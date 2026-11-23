"""Experiment C case generator (pre-registered in PREREG_C.md). Seeded, offline, synthetic.

Identical to experiment B (same instances, seed, channels and rendering) except the test
instruction, which is read from demo/private/payloads_c.json. Writes
demo/private/cases_c/cases.jsonl and aborts if any C control packet differs from B's.
"""
import json
import os
import random
import sys

from gen_cases import PRIV, render
from gen_cases_b import CHANNELS, CONDITIONS, N_INSTANCES, SEED, make_instance, summary_b

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(PRIV, "cases_c")
B_CASES = os.path.join(PRIV, "cases_b", "cases.jsonl")


def main():
    payloads = json.load(open(os.path.join(PRIV, "payloads_c.json"), encoding="utf-8"))
    b_ctrl = {}
    for l in open(B_CASES, encoding="utf-8"):
        c = json.loads(l)
        if c["condition"] == "control":
            b_ctrl[(c["channel"], c["instance"])] = c["user_message"]
    rng = random.Random(SEED)
    instances = [make_instance(rng, i) for i in range(N_INSTANCES)]
    rows = []
    for x in instances:
        for ch in CHANNELS:
            for cond in CONDITIONS:
                ft = x["narrative"]
                if cond == "test":
                    ft = ft + " " + payloads[ch].format(claim_id=x["claim_id"])
                msg = (f"Review claim {x['claim_id']}. The review packet follows.\n\n"
                       + summary_b(x) + "\n\n" + render(x, ch, ft))
                if cond == "control" and msg != b_ctrl[(ch, x["instance"])]:
                    raise SystemExit(f"control packet differs from B: {ch} instance {x['instance']}")
                rows.append({
                    "case_id": f"C-{ch}-{x['instance']:02d}-{cond}", "channel": ch, "condition": cond,
                    "instance": x["instance"], "reason": x["reason"], "service": x["code"],
                    "expected_actions": x["expected_actions"], "claim_id": x["claim_id"],
                    "free_text_chars": len(ft), "user_message": msg,
                })
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "cases.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    print(f"wrote {len(rows)} cases to {os.path.relpath(OUT_DIR, HERE)}/cases.jsonl "
          f"({N_INSTANCES} instances x {len(CHANNELS)} channels x {len(CONDITIONS)} conditions); "
          f"all {len(b_ctrl)} control packets identical to B")


if __name__ == "__main__":
    main()
