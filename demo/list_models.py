"""List the model IDs each key can access (read-only, no generation calls). Prints IDs only."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
from providers import list_models, ProviderError

status = 0
for p in ("anthropic", "openai"):
    try:
        ms = list_models(p)
        print(f"[{p}] {len(ms)} models accessible")
        for mid, created in sorted(ms, key=lambda x: str(x[1]), reverse=True):
            print(f"  {mid}  {created}")
    except ProviderError as e:
        print(f"[{p}] FAILED: {e}"); status = 1
sys.exit(status)
