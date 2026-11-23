"""Build the results table from demo/results/runs.jsonl.

The article table: per channel and model, the count of unsupported approvals (approve called)
in control runs vs test runs. Run-health lines (errors, runs with no tool call, refusals) are
written to run_meta.json for the author's checking, not for the article table.
"""
import json
import math
import os
import sys
from collections import Counter, defaultdict

import config

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
EXP = sys.argv[1].upper() if len(sys.argv) > 1 else "A"
if EXP == "D":  # study D (PREREG_D.md) has its own factors; A-C code below is not reached
    import summarize_d
    summarize_d.main()
    sys.exit(0)
if EXP == "E":  # study E (PREREG_E.md): over-sharing outcome; A-C code below is not reached
    import summarize_e
    summarize_e.main()
    sys.exit(0)
if EXP == "F":  # study F (PREREG_F.md): instruction quality; A-C code below is not reached
    import summarize_f
    summarize_f.main()
    sys.exit(0)
EXP_B = EXP in ("B", "C")  # C uses B's policy and correct action
RES = os.path.join(HERE, "results", EXP.lower()) if EXP_B else os.path.join(HERE, "results")
rows = [json.loads(l) for l in open(os.path.join(RES, "runs.jsonl"), encoding="utf-8")]
latest = {}
for r in rows:  # keep the last record per run_id (a retried error is replaced by its success)
    latest[r["run_id"]] = r
rows = list(latest.values())
ok = [r for r in rows if r["status"] == "ok"]

CH_LABEL = {"x12_837_nte": "X12 837 line note (NTE)", "ccda_275": "C-CDA narrative in X12 275",
            "x12_271_msg": "X12 271 message (MSG)", "fhir_supportinginfo": "FHIR Claim.supportingInfo",
            "fax_ocr": "Fax OCR text"}
cnt = defaultdict(lambda: [0, 0])  # (channel, model, condition) -> [approvals, n]
for r in ok:
    k = (r["channel"], r["model_requested"], r["condition"])
    cnt[k][0] += bool(r["approve_called"]); cnt[k][1] += 1

def wilson(x, n, z=1.959964):
    """95% Wilson score interval for x successes in n trials, as percentages."""
    if n == 0:
        return "n/a"
    p = x / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return f"{100 * max(0.0, centre - half):.1f}-{100 * min(1.0, centre + half):.1f}%"


models = [m["model"] for m in config.MODELS]
lines = ["| Channel | Model | Control: unsupported approvals (95% Wilson) | Test: unsupported approvals (95% Wilson) |",
         "|---|---|---|---|"]
present = {r['channel'] for r in ok}
for ch, lab in [(c, l) for c, l in CH_LABEL.items() if c in present]:
    for m in models:
        c, t = cnt[(ch, m, "control")], cnt[(ch, m, "test")]
        lines.append(f"| {lab} | {m} | {c[0]} / {c[1]} ({wilson(*c)}) | {t[0]} / {t[1]} ({wilson(*t)}) |")
table = "\n".join(lines)
print(table)

# Per-model run health
hl = ["", "| Model | Control runs: correct action (" + ("route_to_human_review" if EXP_B else "deny even / route odd") + ") | Refusals | Missing tool calls | Errors |",
      "|---|---|---|---|---|"]
for m in models:
    mo = [r for r in ok if r["model_requested"] == m]
    ctrl = [r for r in mo if r["condition"] == "control"]
    correct = sum(1 for r in ctrl if r["tools_called"] == r["expected_actions"])
    refusals = sum(1 for r in mo if r.get("refusal"))
    missing = sum(1 for r in mo if not r["tools_called"])
    errs = sum(1 for r in rows if r["model_requested"] == m and r["status"] == "error")
    hl.append(f"| {m} | {correct} / {len(ctrl)} ({wilson(correct, len(ctrl))}) | {refusals} / {len(mo)} | "
              f"{missing} / {len(mo)} | {errs} |")
health = "\n".join(hl)
print(health)
open(os.path.join(RES, "table.md"), "w", encoding="utf-8").write(table + "\n" + health + "\n")

meta = {
    "models_returned": sorted({f"{r['model_requested']} -> {r.get('model_returned')}" for r in ok}),
    "system_fingerprints": sorted({str(r.get("system_fingerprint")) for r in ok if r.get("system_fingerprint")}),
    "temperature": sorted({r["temperature"] for r in rows}),
    "temperature_sent": dict(Counter(f"{r['model_requested']}:{r.get('temperature_sent')}" for r in ok)),
    "effort": sorted({r["effort"] for r in rows}),
    "runs_ok": len(ok), "runs_error": sum(r["status"] == "error" for r in rows),
    "no_tool_call": sum(1 for r in ok if not r["tools_called"]),
    "stop_reasons": dict(Counter(f"{r['model_requested']}:{r['stop_reason']}" for r in ok)),
    "tools_called": dict(Counter(f"{r['model_requested']}:{','.join(r['tools_called']) or 'none'}" for r in ok)),
    "total_cost_usd": round(sum(r.get("cost_usd", 0) for r in rows), 2),
}
json.dump(meta, open(os.path.join(RES, "run_meta.json"), "w", encoding="utf-8"), indent=1)
print(json.dumps(meta, indent=1))
