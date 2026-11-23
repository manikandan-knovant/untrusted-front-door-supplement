# Standards traceability matrix

This matrix lists each data format the catalog treats as an entry surface, with:
- the free-text element an agent can read;
- the source that supports the element;
- whether its use depends on the program or trading partner;
- the catalog entries that use it;
- a confidence level.

It is written from the project's source notes and reasoning log (R-24, R-30, R-31, R-33).
Where those records are silent, the matrix says "not recorded".

## Confidence levels

Confidence is about the **documentary support for the element**: does the free-text element
exist as described? It is not about evidence that anyone has used the element in an attack.
No peer-reviewed source analyzes X12, HL7 v2 or C-CDA as agent entry surfaces (R-22). The
only X12 security source is one automated, non-peer-reviewed audit finding about 837 free
text (G01).

- **High:** the element was read verbatim in a standards page, government companion guide or
  federal rule.
- **Medium:** the element exists, but its use varies by program, or the field that carries
  the text was not shown, or the surface rests on an inference about how documents reach
  the agent.
- **Low:** the element was not verified in any document read.

## Sources

| ID | Source | Read |
|---|---|---|
| STD01 | X12 transaction sets page (x12.org) | Full page; the 834, 835 and 837 names came through the fetch tool's summary |
| STD02 | HL7 Version 2 to FHIR segment maps (HL7) | Full index page; the NTE map page returned 404 |
| STD03 | CDA Section class, CDA v2.0.3 (HL7) | Full page |
| STD04 | FHIR R4 Claim and ClaimResponse resources (HL7) | Full pages, but about 100k characters of each were not read verbatim |
| STD05 | Government X12 companion guides: CMS HETS 270/271 (v16.0, 2026); CMS esMD 278 (v19.0, Jan 2026); Wisconsin Medicaid 278 (v1.1, Sep 2025); North Dakota Medicaid 278 (May 2023); Nebraska Medicaid 278 (v2.00); Wisconsin Medicaid 837P (v2.0, Jun 2025); Nebraska Medicaid 837P (v5.00, 2015) | Full text by script extraction and keyword search; only the cited passages read closely |
| REG01 | CMS-0057-F, 89 FR 8758 (8 Feb 2024), final rule | Summary read closely; full text searched by keyword |
| REG02 | CMS-0053-F, 91 FR 14350 (24 Mar 2026), final rule; compliance by 26 May 2028 | Full text by script extraction and keyword search |
| G01 | Automated third-party audit of a public claims-analytics agent skill (Jul 2026) | Full page; grey literature, motivation only |
| S06, S11, S33, S35 | Research sources on fax, scanned and OCR channels | See the article's references |

**Not retrieved:** the HL7 Da Vinci Prior Authorization Support (PAS) FHIR implementation
guide. Its pages returned no body text, so its content is not described (R-24, R-33). The X12
implementation guides (TR3s) themselves were not read (R-30).

## Matrix

| Format and free-text element | Supporting source | Program dependency | Catalog entries | Confidence |
|---|---|---|---|---|
| **X12 270** eligibility inquiry: none. The guide defines no free-form message element in the request. | STD05 (CMS HETS 270/271 guide) | Only one federal program's guide was read; other programs not recorded | None. T-027 was first written for the 270 and moved to the 271 (R-30). | Medium (absence shown in one guide only) |
| **X12 271 MSG** eligibility response: loop 2110C, MSG01 "Free-form Message". HETS returns an SSA/RRB address "in the exact format received" when it cannot parse it. | STD05 (CMS HETS 270/271 guide) | Shown for the federal HETS program; other programs not read | T-027 | High |
| **X12 278 MSG** services review: MSG at 2000E/2000F, free-form text in the standard | STD05 (CMS esMD, Wisconsin, North Dakota and Nebraska 278 guides) | Varies by program. Wisconsin does not use 2000E/2000F MSG. CMS esMD restricts request MSG01 to codes (ASC, HOPD) and uses response MSG for free-form reason statements. North Dakota's sample files carry MSG text. Nebraska: no MSG found by keyword search of the extracted guide text (checked for this matrix, 2026-11-23). | T-001 (request, conditional); T-052 (response) | Medium |
| **X12 837P NTE** claim: 2400 NTE, NTE02 "Line Note Text". The 2300 claim-level NTE is not confirmed in the guides read. | STD05 (Nebraska 837P guide); G01 (837 free text flagged as an indirect-injection risk) | Wisconsin uses 2400 NTE for program-specific indicators. The 2300 claim note could not be checked: a state document naming it could not be downloaded. | T-014; T-058 | High (2400 line note); Low (2300 claim note) |
| **X12 275 with C-CDA** additional information (attachment): the C-CDA document it carries, with its narrative. In the 278 and 837, PWK carries the attachment control number that links documentation sent separately. | REG02 (adopts X12N 275, 006020X314, and C-CDA R2.1 for claims attachments); STD05 (PWK; esMD links to an X12N 275 or an XDR document); STD03 (narrative) | Claims: national standard, compliance by 26 May 2028. Prior authorization: no attachment standard adopted. Only where programs accept 275s (esMD does, R-31). | T-053 (claims); T-051 (prior authorization) | High (claims); Medium (prior authorization) |
| **X12 277 RFAI** request for additional information: which element carries the request's wording is not recorded (the 277 implementation guide was not read) | REG02 (adopts X12N 277, 006020X313, for claims attachments) | Claims only. The final rule did not adopt the 277 for prior-authorization requests; there, the request travels as 278 response MSG text (R-31). | T-054 | Low (free-text element not verified; adoption of the transaction is verified) |
| **HL7 v2 NTE** "Notes and Comments" segment, attached to results and orders, mapped to FHIR DocumentReference, Observation and ServiceRequest | STD02 | Not recorded. Local interface use was not examined. The field carrying the comment text is not stated on the page read. | T-013; T-045; T-032 (registration messages with "comments"; segment not named) | Medium |
| **C-CDA narrative block**: CDA Section "text" (0..1, xhtml), "Narrative to be rendered", alongside coded entries | STD03; REG02 (C-CDA R2.1 adopted for claims attachments) | National for claims attachments from 2028. Elsewhere depends on the exchange. | T-002; T-012; T-044; T-051; T-053 | High |
| **FHIR Claim.supportingInfo**: supportingInfo.value[x], including valueString ("Data to be provided") | STD04 (FHIR R4 Claim); REG01 (Prior Authorization API required of impacted payers in 2027) | Impacted payers under CMS-0057-F, from 2027. The FHIR prior-authorization IG (PAS) was **not retrieved**, so the element carrying text in a prior-authorization request is unverified (R-33). | T-016 (claim); T-005 (prior-authorization interface) | High (base R4 resource); Low (prior-authorization requests, IG not retrieved) |
| **FHIR ClaimResponse.processNote**: processNote.text ("Note explanatory text"), a human-readable adjudication explanation; also a disposition string | STD04 (FHIR R4 ClaimResponse); REG01 (prior-authorization information added to the Patient Access API) | Patient Access API under CMS-0057-F. Whether payers populate processNote is not recorded. | T-057 | High |
| **FHIR, element not specified**: "a free-text element" in payer-to-payer data, or "content in a retrieved FHIR resource" | REG01 (Payer-to-Payer API); STD04; S06 (cross-institutional FHIR endpoints named as a clinical channel); S30 (contaminated FHIR resources) | Payer-to-Payer API under CMS-0057-F, from 2027 | T-004; T-046 | Medium |
| **Fax/OCR**: no structured element. Page images are converted to text by OCR, including text a human reviewer cannot see on the page. | REG02 (claims attachments still rely largely on fax, mail or portal uploads); STD05 (Nebraska 837P PWK instructions give a fax number; 278 attachments can go by fax under some programs); S33, S35 (hidden text in images steers medical vision-language models); S06, S11 (fax named as a clinical channel) | Common but not universal (REG02). The OCR evidence comes from clinical imaging, not administrative documents (R-12). | T-003; T-024; T-049; T-055 | Medium |

## Further X12 entries not tied to one free-text element

| Entry | What it relies on | Support | Confidence |
|---|---|---|---|
| T-022 | Content of a submitted claim file as a whole (clearinghouse code generation) | G01; STD01 | Medium |
| T-031 | Content of an 834 enrollment file | STD01 names the 834 (via the fetch tool's summary). Its free-text elements were not read. | Low |
| T-056 | A provider's own past claims (billing pattern, not a text element) | STD01; ADV01 | Not applicable: no free-text element is claimed |

## What the matrix does not show

- How often any of these elements carries free text in production traffic. This was not
  examined and varies by program and partner (article, Limitations).
- Commercial trading-partner rules, which were deliberately not consulted: government
  sources only, by author instruction (R-30).
- Test results. The article's six studies placed planted text in some of these channels;
  see `demo/` for the designs and results.
