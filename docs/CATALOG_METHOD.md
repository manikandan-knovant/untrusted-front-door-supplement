# How the threat catalog was built

This note explains how the 58 entries in [`threat_catalog.yaml`](../threat_catalog.yaml) were
produced: how candidates were generated, added, rejected and revised; how entries were kept
distinct; how the OWASP class was assigned; and how the entries were checked. It closes with
three fully worked entries.

It is written from the project's records: the reasoning log (entries R-1 to R-38), the
outline, the novelty report, the catalog itself and its checker, and the article text
(draft v7). Where the records are silent, this note says "not recorded". The records are not
part of this release. R-numbers are given so that statements can be traced by editors and
reviewers on request.

## AI assistance and the author's role

The catalog was first drafted with Anthropic's Claude (Claude Code) and then verified and
revised by the author. The article's Acknowledgments states that Claude was used "to draft
the initial threat catalog", and that the author "verified every claim against its cited
sources, revised all AI-drafted content, and takes full responsibility for the article".

## 1. Unit of analysis

The recorded rule (R-23, heading):

> "Each catalog row is one wrong thing an agent does, entering through one surface and mapped
> to one primary ASI entry"

The article states the same rule: "Each entry records one threat to one agent. It names the
entry surface the threat comes through, one primary OWASP entry, the actor, the operator
(whose agent it is: payer, provider, intermediary, or consumer), and the impact: integrity,
confidentiality, or both."

Every entry has ten fields: `id`, `workflow`, `operator`, `actor`, `owasp_asi`,
`entry_surface`, `scenario`, `impact_type`, `source`, `reasoning_ref`. Scenarios describe
threats and impact types only. They contain no attack payloads, field-level exploitation
steps or test procedures (R-23).

## 2. How candidates were generated

- **Threat classes came from the sources** (R-23):
  - injection through data (F01, S06, S11, S32);
  - memory and knowledge poisoning (S24, S60);
  - tool misuse (S39, S67);
  - delegation and identity (S61, S29);
  - inter-agent communication (S64);
  - cascades (S62);
  - sycophancy and over-trust (S63, S65);
  - supply chain and tool metadata (S60, S69);
  - code execution (S05, F01);
  - drift and rogue behavior (S60, S26, S68);
  - planted false content (S70).
- **Placement was author analysis.** Each class was placed in a workflow (prior
  authorization, claims, eligibility, member service, or clinical documentation as a
  contrast) and on an entry surface (X12, HL7 v2, C-CDA, FHIR, fax/OCR, human channels, or
  agent internals). R-23 states: "Placing a class in a payer workflow and on a named entry
  surface is my own analysis, and so is every scenario sentence [author analysis]."
- **Constraints enforced by the checker:** all of ASI01 to ASI10 must appear, and each
  workflow must have at least 5 entries.
- **Not recorded:**
  - the list of candidate threats before the first catalog version;
  - how many candidates there were;
  - the order in which classes were placed.

## 3. Additions, rejections and revisions

The records show the following changes after the first catalog version.

**Added:**

| Entry | What | Record |
|---|---|---|
| T-051 | 275 carrying C-CDA for prior authorization, where programs accept 275s | R-30, R-31 |
| T-052 | Provider agent reading the request for more information in a 278 response | R-31 |
| T-053 | 275 with C-CDA claims attachment | R-31 |
| T-054 | Spoofed 277 request for more information read by a provider billing agent | R-31 |
| T-055, T-056 | Payment-integrity entries | R-32 |
| T-057 | Member's own assistant reading patient-access data | R-31 |
| T-058 | Clearinghouse claim-editing agent | First named in R-30; when it was added is not recorded |

**Rejected, as recorded:**

| What was rejected | Reason recorded | Record |
|---|---|---|
| T-027 as first written (free text in the 270 inquiry) | The companion guides show no free text in the 270; replaced by the 271 free-form message | R-30 |
| Using a 277 as the prior-authorization request for information | The final attachments rule adopted the 277 for claims only | R-31 |
| Keeping T-005 on X12, with the attachment path as justification | "Rejected because T-051 now covers that path" | R-33 |
| A separate "payment_integrity" workflow | Keeps the five-value workflow list | R-32 |
| More speculative eligibility entries | Eligibility already had 7 | R-27 |
| Dropping the clinical contrast entries | The brief asks for a contrast section, and the check needs 5 per workflow | R-26 |
| Dropping X12 entries that lacked segment-level sourcing | They are what the novelty claim is about; kept with a weak-point flag | R-24 |
| Dropping T-001 | At least one state's samples carry 278 message text; the entry now states the condition | R-30 |
| Dropping T-056 | Kept, with a plain statement that the threat is not unique to LLM agents | R-35 |
| Multi-label OWASP mapping | A single primary class keeps the figure and table readable | R-23 |

**Revised:**

| Change | Record |
|---|---|
| Impact vocabulary changed to integrity, confidentiality or both (author instruction) | R-28 |
| Actor and operator fields added to every entry | R-29 |
| X12 entries revised after the companion-guide check (section 6) | R-30 |
| New entry surface "internal" for drift entries with no external channel; T-005 moved to the FHIR prior-authorization interface | R-33 |
| Actor "none" used only for the three drift entries, and tied to surface "internal" by the checker (author decision) | R-36 |

**Merged:** no merge of two candidate entries into one is recorded.

## 4. Deduplication: the rule actually applied

**No deduplication rule is recorded in the project's records.** The response to reviewers
describes one: "the deduplication rule (one entry per agent, entry surface and harm)". That
wording does not appear in the reasoning log, the outline, the novelty report or the article
draft. The records contain only the unit-of-analysis rule in section 1 (R-23) and one
decision about overlap (R-33).

**Evidence from the records:**

1. The unit of analysis (R-23): "Each catalog row is one wrong thing an agent does, entering
   through one surface and mapped to one primary ASI entry". The outline restates it:
   "Unit of analysis: one threat to one agent, entering through one surface." Neither names
   harm, or impact, as a key for keeping entries apart.
2. The one recorded overlap decision (R-33): keeping T-005 on X12 "with the attachment path
   as justification" was "Rejected because T-051 now covers that path". So an entry was not
   kept on a delivery path that another entry already covered.
3. The catalog keeps entries that "one entry per agent, entry surface and harm" would merge.
   T-002 and T-051 share every coded field (workflow `prior_authorization`, operator
   `payer`, actor `provider_fraud`, `ASI01`, surface `ccda`, impact `integrity`), and both
   scenarios name "the review agent":
   - T-002: "Directive text sits in the human-readable narrative of a C-CDA document
     submitted as clinical evidence. The review agent treats it as reviewer guidance ..."
   - T-051: "Supporting documentation for a pended prior-authorisation request arrives as an
     X12 275 carrying a C-CDA document, linked to the request by its attachment control
     number. Narrative text in the document leads the review agent to treat the request as
     fully documented ..."

   Same agent, same entry surface, same harm: under the stated rule these would be one
   entry. They differ only in the delivery path (a submitted C-CDA document, or a 275
   linked by an attachment control number). R-30 records that this path "motivated T-051".
4. One other pair shares every coded field: T-024 and T-055 (claims, payer,
   provider_fraud, ASI01, fax_ocr, integrity). These two are different agents: a claims
   review agent and a post-payment payment-integrity agent. So the pair is consistent with
   the stated rule.

**What can be said about the rule applied** (derived from the evidence above, not a
recorded rule):
- entries were kept separate when they differed in workflow, operator, entry surface,
  primary OWASP class, actor or impact type;
- entries were also kept separate when all of those matched but the agent (T-024, T-055)
  or the delivery path within a surface (T-002, T-051) differed;
- one entry was moved so that two entries would not cover the same delivery path (R-33).

**Conclusion.** The rule stated in the response to reviewers, "one entry per agent, entry
surface and harm", does not match the records, and the catalog contains a pair (T-002,
T-051) that it would merge. Either that wording or the catalog needs to change. This note
does not choose between them.

## 5. OWASP assignment order

The OWASP class names come from the OWASP announcement page (O01). The primary OWASP
document was not retrieved, so the rules below are a reading of the entry names, not the
OWASP definitions (R-25). They were applied in this order (R-25):

1. **ASI01** when untrusted content redirects the agent's goal within one interaction.
2. **ASI06** when the content persists in memory or knowledge and affects later decisions,
   including cross-session bleed.
3. **ASI02** when the agent misuses a tool it legitimately holds.
4. **ASI03** when the harm comes from identity, delegation or over-broad privilege.
5. **ASI04** when an upstream component (content package, skill, parser, tool description)
   is altered.
6. **ASI05** when generated code runs.
7. **ASI07** when messages between agents lack authenticated sender or integrity.
8. **ASI08** when one wrong output propagates through other agents.
9. **ASI09** when a human over-trusts the agent.
10. **ASI10** when the agent drifts beyond its approved scope or outlives it.

**How the order was applied.** The questions were not used as a strict first-match rule,
where the first class that fits wins. For each entry, the recorded class is the one that
names the core of the threat. The author states this for this release. The article gives
the same principle for one case: "Tool misuse after an injection, for example, is recorded
as ASI02 only when the misuse of a held tool is the core of the threat." So an entry whose
threat starts with untrusted content can carry a later class, such as ASI02, ASI03 or ASI07,
when that class names what goes wrong. R-25 records two entries that fit two classes: T-005 (ASI01 and ASI02) and T-021
(ASI04 and ASI01). [`ASI_ALTERNATIVES.md`](ASI_ALTERNATIVES.md) lists secondary classes for
the borderline entries. No inter-rater reliability was measured.

Actor and operator were assigned by two questions (R-29). The actor answers "who benefits,
or who causes the input to be malicious?". The operator answers "whose agent does the
harmful thing?".

## 6. Verification

**What the records show was checked:**

1. **Companion-guide check of the X12 entries** (R-30). Government companion guides were read
   (author instruction: government sources only): CMS HETS 270/271, CMS esMD 278,
   Wisconsin, North Dakota and Nebraska Medicaid 278, and Wisconsin and Nebraska Medicaid
   837P. The resulting changes:
   - **T-027 (rewritten):** first written about free text in the 270 eligibility inquiry.
     "Dropped as written, because the guides show no free text in the 270", and replaced by
     the 271 free-form message read by a provider-side registration agent (operator
     provider, actor upstream_supplier).
   - **T-001 (rewritten):** 278 request free text. "Kept, but scoped to programs that allow
     free-form request MSG text. The variability is stated in the scenario." The scenario
     now opens "In programs whose companion guides let a 278 request carry free-form message
     text" and ends "the exposure depends on trading-partner rules".
   - **Also changed:** T-005 moved off X12 to the FHIR prior-authorization interface (R-30,
     R-33). T-014 and T-058 now say "line-note" text, which is the 837 element the guides
     verify.

   These are the "two entries that the guides did not support" in the article (T-001 and
   T-027, as named in R-30's heading). The wording of T-001 and T-027 before the rewrite is
   not recorded in the files this note was written from.
2. **Regulatory status** was checked against the Federal Register (R-31):
   - CMS-0057-F (FHIR interfaces from 2027; prior-authorization timeframes from 2026);
   - CMS-0053-F, a final rule (275, 277 request for additional information and C-CDA for
     claims attachments; compliance by 26 May 2028; no prior-authorization attachment
     standard).

   T-051 to T-054 follow that scope.
3. **Automated checks:** `check_catalog.py` (not in this release, because it reads the
   private literature notes). On 2026-11-23 the catalog in this release, byte-identical to
   the checked file, passed all 11 checks:
   - strict parse;
   - required fields and allowed values;
   - unique IDs;
   - all ten ASI classes present;
   - at least 5 entries per workflow;
   - no person, customer or company names;
   - no measurement words;
   - no retired wording;
   - every cited source has a note;
   - every reasoning reference exists;
   - every actor and operator value used, with actor "none" if and only if surface
     "internal".
4. **Author decisions recorded in the log:**
   - the angle (outline);
   - the impact vocabulary (R-28);
   - government-only companion guides (R-30);
   - the actor value "none" (R-36);
   - the reference changes (R-37).

   The author also supplied two full texts (S03, S06) that automated retrieval could not
   reach.
5. **The author's own verification:** the article's Acknowledgments states that the author
   verified every claim against its cited sources and revised all AI-drafted content.

**Not recorded:**
- a per-entry log of the author's verification (which entry was checked, against which
  source, on what date);
- which entries the author revised, and how.

## 7. Three worked entries

Each entry is quoted from `threat_catalog.yaml` exactly, then explained field by field. The
catalog uses British spelling; quotations keep it.

### T-052: request for more information in a 278 response (prior authorization, provider side)

```
id: T-052
workflow: prior_authorization      operator: provider      actor: trading_partner
owasp_asi: ASI01                   entry_surface: x12      impact_type: confidentiality
source: STD05; REG02; ADV02; F01
reasoning_ref: R-23; R-29; R-30; R-31
scenario: "A provider-side agent assembles documentation in response to a payer's request for
additional information on a pended prior authorization. That request is carried as free-form
reason text in a 278 response, since the 277-based request was adopted only for claims.
Request text altered by a compromised intermediary leads the agent to send far more of the
record than the request needs, or to send it to an unexpected destination."
```

- **Agent and workflow:** a provider-side agent that answers a payer's request for
  documentation on a pended prior authorization.
- **Entry surface (x12):**
  - the CMS esMD 278 guide uses the response MSG segment for free-form reason statements
    and restricts request MSG01 to codes (STD05);
  - the attachments rule adopted the 277 request for additional information for claims
    only, and no prior-authorization attachment standard (REG02).

  So for prior authorization, the request for more information travels as 278 response text
  (R-31).
- **Actor (trading_partner):** a compromised intermediary alters the request in transit. It
  is grounded in the CMS report of the February 2024 cyberattack that took a health care EDI
  company offline (ADV02).
- **Operator (provider):** the failing agent is the provider's (R-29).
- **ASI01:** untrusted request text redirects the agent's task within one interaction
  (assignment rule 1). The mechanism, instructions in retrieved data steering an LLM
  application, is from F01. The alteration by an intermediary also fits ASI07; see
  [`ASI_ALTERNATIVES.md`](ASI_ALTERNATIVES.md).
- **Impact (confidentiality):** the agent over-shares records, or sends them to the wrong
  destination.
- **History:** added with the claims-attachment entries after the final rule was checked
  (R-31).
- **Testing:** the article reports that this is the one entry shown to occur in a toy agent.
  - Study E tested it through X12 278 and FHIR text, under a numbered policy: 800 runs, no
    target actions.
  - Study F reran the task. With a one-line prompt, one model attached documents outside
    the request in 31 of 50 test runs and in none of 50 controls. With explicit rules, no
    model did.

  See `demo/` for the designs and results.
- **Limits:**
  - 278 message use varies by program (R-30; confidence Medium for 278 message prevalence);
  - the X12 implementation guides themselves were not read.

### T-005: tool misuse through the FHIR prior-authorization interface (payer side)

```
id: T-005
workflow: prior_authorization      operator: payer         actor: provider_fraud
owasp_asi: ASI02                   entry_surface: fhir     impact_type: integrity
source: REG01; STD04; S39; S67; F01
reasoning_ref: R-23; R-25; R-33
scenario: "A request arrives through the FHIR prior-authorisation interface that payers must
offer from 2027, and its supporting-information strings steer an agent holding legitimate
write access to the utilisation-management system. The agent extends approved units or date
spans beyond the request, or updates a different authorisation."
```

- **Agent and workflow:** a payer agent with legitimate write access to the
  utilization-management system.
- **Entry surface (fhir):**
  - CMS-0057-F requires impacted payers to offer a FHIR Prior Authorization API, with
    compliance in 2027 (REG01);
  - the base FHIR R4 Claim resource carries `supportingInfo` values, including strings
    (STD04).

  The FHIR prior-authorization implementation guide was **not retrieved**, so the exact
  element that carries text in a prior-authorization request is unverified (R-33).
- **Actor (provider_fraud):** the requester gains from wider approvals (R-29).
- **Operator (payer).**
- **ASI02 (primary), ASI01 (alternative):** the core of the threat is misuse of a tool the
  agent legitimately holds (rule 3, and the article's tie-break). An injection starts it,
  so ASI01 also fits. R-25 names this entry as fitting both. Tool-misuse grounding: S39
  (tool abuse in a clinical agent, mapped to ASI02) and S67 (prompts that trigger harmful
  database queries; abstract only).
- **Impact (integrity):** wrong authorization records.
- **History:**
  - first placed on X12 (278 request free text);
  - the companion guides showed 278 request text is often unused or restricted (R-30);
  - moved to the FHIR interface, because keeping it on X12 with the attachment path would
    have duplicated T-051 (R-33).
- **Testing:** not tested. No study in the article targets this entry.
- **Limits:**
  - the prior-authorization implementation guide was not retrieved;
  - the scenario is reasoned, not observed (R-23).

### T-055: records under review steer the payment-integrity agent (claims)

```
id: T-055
workflow: claims                   operator: payer         actor: provider_fraud
owasp_asi: ASI01                   entry_surface: fax_ocr  impact_type: integrity
source: ADV01; REG02; S33; S35; F01
reasoning_ref: R-23; R-29; R-32
scenario: "A payment-integrity agent reviews records a provider submitted, often by fax, for
a post-payment fraud, waste and abuse review. Text in the records addressed to the reviewer
leads the agent to close the review as supported, so the content under review steers the
review."
```

- **Agent and workflow:** a payer's payment-integrity agent doing post-payment fraud, waste
  and abuse review. It is recorded under workflow "claims", because a separate workflow was
  rejected (R-32).
- **Entry surface (fax_ocr):**
  - the attachments rule states that claims attachments still rely largely on fax, mail or
    portal uploads (REG02);
  - text embedded in images, including text a human cannot see that OCR still reads, has
    steered medical vision-language models (S33, S35).
- **Actor (provider_fraud):** the provider under review writes the evidence the agent
  reads. Provider fraud is grounded in the HHS-OIG 2025 national takedown: 324 defendants
  and over $14.6 billion in intended loss (ADV01).
- **Operator (payer).**
- **ASI01:** text in the records redirects the review within one interaction (rule 1). The
  mechanism is F01.
- **Impact (integrity):** a fraudulent claim's review is closed as supported.
- **History:** added with T-056 as the payment-integrity pair (R-32). R-32 records that
  "Fraud, waste and abuse review is the one workflow where the party under review writes the
  evidence the agent reads".
- **Testing:** not tested as this entry. The article's studies A to D used a payer
  claims-review agent, and the article does not map them to T-055.
- **Limits:** "No source documents an AI payment-integrity agent being attacked" (R-32).
  Records may also arrive as uploads or 275 attachments rather than by fax. The entry uses
  fax/OCR as its single surface.
