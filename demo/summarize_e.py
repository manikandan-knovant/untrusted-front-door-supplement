"""Study E tables (PREREG_E.md), called by `python summarize.py E`. Reads demo/results/e/runs.jsonl."""
import json
import os
from collections import Counter, defaultdict

from summarize_d import wilson

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results", "e")
MODELS = ["claude-sonnet-5-5", "gpt-6.2-sol", "claude-haiku-5-5", "gpt-6-luna"]
CH_LABEL = {"x12_278_msg": "X12 278 response MSG", "fhir_processnote": "FHIR ClaimResponse.processNote"}


def main():
    rows = {}
    for l in open(os.path.join(RES, "runs.jsonl"), encoding="utf-8"):
        r = json.loads(l)
        rows[r["run_id"]] = r  # last record per run_id
    rows = list(rows.values())
    ok = [r for r in rows if r["status"] == "ok"]
    cnt = defaultdict(lambda: [0, 0])
    for r in ok:
        k = (r["model_requested"], r["channel"], r["condition"])
        cnt[k][0] += bool(r["overshare"]); cnt[k][1] += 1
    lines = ["| Model | Channel | Control: over-sharing runs (95% Wilson) | Test: over-sharing runs (95% Wilson) |",
             "|---|---|---|---|"]
    for m in MODELS:
        for ch, lab in CH_LABEL.items():
            c, t = cnt[(m, ch, "control")], cnt[(m, ch, "test")]
            lines.append(f"| {m} | {lab} | {c[0]} / {c[1]} ({wilson(*c)}) | {t[0]} / {t[1]} ({wilson(*t)}) |")
    table = "\n".join(lines)
    print(table)
    hl = ["", "| Model | Control runs: sent exactly the requested documents | Refusals | Missing send_response | Errors |",
          "|---|---|---|---|---|"]
    for m in MODELS:
        mo = [r for r in ok if r["model_requested"] == m]
        ctrl = [r for r in mo if r["condition"] == "control"]
        exact = sum(1 for r in ctrl if r.get("exact_request"))
        refusals = sum(1 for r in mo if r.get("refusal"))
        missing = sum(1 for r in mo if not r.get("sent"))
        errs = sum(1 for r in rows if r["model_requested"] == m and r["status"] == "error")
        hl.append(f"| {m} | {exact} / {len(ctrl)} ({wilson(exact, len(ctrl))}) | {refusals} / {len(mo)} | "
                  f"{missing} / {len(mo)} | {errs} |")
    health = "\n".join(hl)
    print(health)
    open(os.path.join(RES, "table.md"), "w", encoding="utf-8").write(table + "\n" + health + "\n")
    meta = {
        "models_returned": sorted({f"{r['model_requested']} -> {r.get('model_returned')}" for r in ok}),
        "temperature": sorted({r["temperature"] for r in rows}),
        "temperature_sent": dict(Counter(f"{r['model_requested']}:{r.get('temperature_sent')}" for r in ok)),
        "effort": sorted({r["effort"] for r in rows}),
        "max_tokens": sorted({r["max_tokens"] for r in rows}),
        "runs_ok": len(ok), "runs_error": sum(r["status"] == "error" for r in rows),
        "missing_send_response": sum(1 for r in ok if not r.get("sent")),
        "stop_reasons": dict(Counter(f"{r['model_requested']}:{r['stop_reason']}" for r in ok)),
        "sensitive_note_shared": dict(Counter(f"{r['model_requested']}:{r['condition']}" for r in ok
                                              if r.get("sensitive_shared"))),
        "docs_outside_request_total": _sum_outside(ok),
        "invalid_attach_calls": sum(r.get("invalid_attach", 0) for r in ok),
        "model_calls_per_run": dict(Counter(f"{r['model_requested']}:{r.get('n_calls')}" for r in ok)),
        "total_cost_usd": round(sum(r.get("cost_usd", 0) for r in rows), 2),
    }
    json.dump(meta, open(os.path.join(RES, "run_meta.json"), "w", encoding="utf-8"), indent=1)
    print(json.dumps(meta, indent=1))


def _sum_outside(ok):
    s = Counter()
    for r in ok:
        s[f"{r['model_requested']}:{r['condition']}"] += r.get("n_outside_requested", 0)
    return dict(s)
