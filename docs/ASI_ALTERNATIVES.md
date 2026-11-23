# Alternative OWASP classes for borderline entries

Each catalog entry carries one primary class from the OWASP Top 10 for Agentic Applications
(field `owasp_asi`). The article states that many entries fit two classes, and that the
primary one is recorded. This note lists, for the borderline entries, the primary class, a
plausible secondary class, and a one-line reason.

**No inter-rater reliability was measured, and none is claimed.** Every primary class was
assigned by a single process: drafted with Anthropic's Claude, then verified and revised by
the author. They are judgments, not measurements.

## How the secondary classes were chosen

- **Recorded by the author (R-25):** the project's reasoning log names two entries as
  fitting two classes: T-005 (ASI02 and ASI01) and T-021 (ASI04 and ASI01).
- **Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23:** for every other entry, the scenario
  text was checked, with Claude's assistance, against the assignment questions in
  [`CATALOG_METHOD.md`](CATALOG_METHOD.md#5-owasp-assignment-order). An entry is listed here
  when its own scenario describes the mechanism of a second class. The author reviewed and
  accepted these 23 secondary classes on 2026-11-23.
- **Entries not listed:** no second class was identified from their scenario text. That is
  not a claim that no other class could fit.
- **Not part of the catalog:** secondary classes are not fields in `threat_catalog.yaml`, and
  the catalog is unchanged.

## Table

| Entry | Primary | Plausible secondary | Status | Reason |
|---|---|---|---|---|
| T-005 | ASI02 | ASI01 | Recorded by the author (R-25) | Supporting-information strings steer the agent (ASI01), but misuse of its held write access is the core (ASI02). |
| T-008 | ASI08 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The cascade starts from "a determination steered by submitted content". |
| T-010 | ASI04 | ASI06 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The altered criteria package sits in the agent's knowledge and shapes every later request. |
| T-012 | ASI05 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | A crafted attachment shapes the code the agent writes and runs. |
| T-016 | ASI02 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | Same pattern as T-005: a FHIR supporting-information string leads to misuse of a held tool. |
| T-017 | ASI03 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | A portal message is what gets the over-privileged agent to retrieve and share records. |
| T-019 | ASI08 | ASI06 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The misreading persists in shared knowledge before it propagates. |
| T-021 | ASI04 | ASI01 | Recorded by the author (R-25) | A published tool description (upstream component) carries instructions the agent follows. |
| T-022 | ASI05 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | Content in the submitted claim file shapes the generated parsing code. |
| T-025 | ASI06 | ASI04 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The forged document enters through an upstream intake channel run by a compromised partner. |
| T-028 | ASI03 | ASI07 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The lookup is an agent-to-agent query whose sender is not bound to an encounter. |
| T-031 | ASI02 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | File content from a compromised sponsor system steers the agent's write access. |
| T-034 | ASI01 | ASI02 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The hijacked agent "makes account changes outside its task" with its tools. |
| T-035 | ASI01 | ASI02 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | Indirect instructions end in tool actions: address changes and document reissue. |
| T-038 | ASI02 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The agent is "induced" by the user to use its account tools. |
| T-039 | ASI06 | ASI04 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The benefit documents come from an upstream supplier (actor `upstream_supplier`) and are tampered with before they reach the corpus. |
| T-040 | ASI05 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | Content in the uploaded bill shapes the code the agent generates. |
| T-041 | ASI08 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | "An instruction planted in that conversation" is what travels with the hand-off. |
| T-043 | ASI07 | ASI03 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The payer agent "cannot verify that delegation": an identity and delegation failure. |
| T-045 | ASI06 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | A "directive comment" on a lab result can redirect the drafting agent at once. |
| T-046 | ASI02 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | Content in a retrieved FHIR resource drives the write-back tool use. |
| T-050 | ASI03 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | An impostor's message triggers the release that the standing credentials permit. |
| T-052 | ASI01 | ASI07 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The request text is "altered by a compromised intermediary" in transit. |
| T-054 | ASI07 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | The agent follows the spoofed request's content and over-shares. |
| T-058 | ASI02 | ASI01 | Proposed with AI assistance; reviewed and accepted by the author, 2026-11-23 | Line-note text steers the clearinghouse agent's code edits. |

## Notes on similar entries with different primary classes

The assignment questions were applied by recording the class that names the core of the
threat, not as a strict first-match rule (see
[`CATALOG_METHOD.md`](CATALOG_METHOD.md#5-owasp-assignment-order)). So T-017, T-050 and
T-054 keep ASI03, ASI03 and ASI07, even though untrusted content starts each threat. Two
pairs look alike but carry different primary classes. The author explains them as follows.

- **T-052 (ASI01) and T-054 (ASI07):** T-052 (ASI01): what matters is the altered free-text reason steering the agent. T-054 (ASI07): what matters is that the whole request-for-information message is accepted without verifying who sent it or that it arrived unaltered. ASI07 covers both forgery and tampering on the channel between agents.
- **T-010 (ASI04) and T-039 (ASI06):**
  - In T-010, the altered item is a component the agent loads: a criteria content package,
    an installed skill or a document parser. That is a supply-chain issue.
  - In T-039, the altered item is content the agent retrieves: benefit documents in its
    retrieval corpus. That is knowledge poisoning.

The OWASP class names come from the OWASP announcement page. The primary OWASP document,
with full definitions, was not retrieved, so these assignments rest on a reading of the
entry names (R-25).
