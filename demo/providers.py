"""Minimal HTTPS clients for the two model providers (Python standard library only).

Keys are read at call time from the process environment, falling back to the Windows
user environment (HKCU\\Environment). Keys are never printed, logged or written anywhere.
Error messages carry the HTTP status and the provider's error type/message only.
"""
import json
import os
import time
import urllib.error
import urllib.request

ANTHROPIC_BASE = "https://api.anthropic.com/v1"
OPENAI_BASE = "https://api.openai.com/v1"
ANTHROPIC_VERSION = "2023-06-01"
UA = "lit-review-script/0.1 (research; no contact)"


class ProviderError(Exception):
    pass


def get_key(name):
    v = os.environ.get(name)
    if not v:
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h:
                v = winreg.QueryValueEx(h, name)[0]
        except OSError:
            v = None
    if not v:
        raise ProviderError(f"{name} is missing")
    return v


def _headers(provider):
    if provider == "anthropic":
        return {"x-api-key": get_key("ANTHROPIC_API_KEY"), "anthropic-version": ANTHROPIC_VERSION,
                "content-type": "application/json", "user-agent": UA}
    return {"authorization": "Bearer " + get_key("OPENAI_API_KEY"),
            "content-type": "application/json", "user-agent": UA}


def _safe_error(e):
    try:
        body = json.loads(e.read().decode("utf-8", "replace"))
        err = body.get("error", body)
        if isinstance(err, dict):
            return f"HTTP {e.code}: {err.get('type', '')} {err.get('message', '')}".strip()
    except Exception:
        pass
    return f"HTTP {e.code}"


def request(provider, method, path, body=None, timeout=120, retries=5):
    base = ANTHROPIC_BASE if provider == "anthropic" else OPENAI_BASE
    data = json.dumps(body).encode("utf-8") if body is not None else None
    delay = 2.0
    for attempt in range(retries + 1):
        req = urllib.request.Request(base + path, data=data, method=method, headers=_headers(provider))
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            msg = _safe_error(e)
            if e.code in (429, 500, 502, 503, 504, 529) and attempt < retries:
                time.sleep(delay); delay *= 2; continue
            raise ProviderError(msg) from None
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < retries:
                time.sleep(delay); delay *= 2; continue
            raise ProviderError(f"network error: {type(e).__name__}") from None


def list_models(provider):
    if provider == "anthropic":
        out, after = [], None
        while True:
            q = "/models?limit=1000" + (f"&after_id={after}" if after else "")
            r = request("anthropic", "GET", q)
            out += [(m["id"], m.get("created_at", "")) for m in r.get("data", [])]
            if not r.get("has_more"):
                return out
            after = r.get("last_id")
    r = request("openai", "GET", "/models")
    return [(m["id"], str(m.get("created", ""))) for m in r.get("data", [])]
