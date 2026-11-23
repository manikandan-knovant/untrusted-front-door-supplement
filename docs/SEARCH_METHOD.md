# Search method

This note describes the literature search behind the article's novelty statements: which
sources were searched, when, with which terms, how records were screened, and which
adjacent work was considered and excluded. It is written from the project's search records
(novelty report, reasoning log, search log, screening log and reference shortlist). Where
those records are silent, this note says "not recorded".

The literature notes, full texts and logs themselves are not part of this release (see the
README). Record IDs such as S06 or R-3 refer to those private records and are given so that
statements here can be traced by editors and reviewers on request.

## AI assistance

The searches were run, and the records screened, with Anthropic's Claude (Claude Code) under
the author's direction, as stated in the article's Acknowledgments. The author set the angle,
supplied two full texts that automated retrieval could not reach, asked for specific
additional searches (listed below), and verified the claims the article makes from these
sources.

## Dates and window

- All searches were run on **2026-11-21**.
- Publication window: **2023-01-01 to 2026-11-21**. Earlier records were excluded by date
  (3,347 records, mostly from the PubMed query).
- The IEEE *Security & Privacy* venue sweep covered works published 2025-01-01 to 2026-12-31.

## Sources searched

| Source | How it was queried | Notes |
|---|---|---|
| arXiv API | Boolean queries, categories cs.CR, cs.AI, cs.CL, cs.SE; submitted from 2023-01-01; top 100 by relevance | Queries Q01-Q10 and V01-V10 |
| Semantic Scholar Graph API | Boolean bulk search (first 200 kept), plus author, citation and reference endpoints | Q01-Q10, V01-V10, disconfirmation queries D01-D11, author lookup, snowballing |
| Crossref works API | Relevance ranking only (totals of 0.4 to 3 million per query); top 40 per query kept | Q01-Q10 and V01-V10; mainly a net for journal items |
| PubMed (E-utilities) | One payer query (PM1), run as specified by the author and filtered afterwards | Added before Milestone 2 |
| Crossref, journal ISSN 1540-7993 | All IEEE *Security & Privacy* works 2025-2026, then a title filter | Venue sweep (SP1-SP3); abstracts from Semantic Scholar and OpenAlex |
| General web search | 5 queries (W01-W05) | Used for grey literature and disconfirmation only |
| Federal Register API, government sites, standards sites | Direct lookups | Fact sources for regulations, companion guides, standards and adversary grounding (not research literature) |

**Not searched:** Google Scholar (no API, and scraping was avoided), and the native search
interfaces of IEEE Xplore and the ACM Digital Library. Semantic Scholar indexes these venues,
but many IEEE records there lack abstracts. IEEE Xplore pages returned no content to the
fetch tool, so abstracts for the venue sweep came from Semantic Scholar and OpenAlex.

## Search terms

Each of the ten core queries (Q) and ten variants (V) was run on arXiv, Semantic Scholar and
Crossref. The wording below is the logged query label. The exact per-database strings are in
the private search log.

| ID | Query (as logged) |
|---|---|
| Q01 | "threat model" AND ("LLM agent" OR "agentic AI") AND healthcare |
| Q02 | "risk assessment" AND LLM AND healthcare AND (agent OR tool) |
| Q03 | "prompt injection" AND (FHIR OR HL7 OR "clinical notes" OR EHR) |
| Q04 | "prompt injection" AND (X12 OR claims OR "prior authorization" OR payer) |
| Q05 | ("prior authorization" OR "claims adjudication" OR "health plan" OR payer) AND ("AI agent" OR "LLM agent") |
| Q06 | "OWASP Top 10 for Agentic Applications" OR "OWASP agentic" |
| Q07 | "indirect prompt injection" AND (document OR OCR OR fax OR attachment) AND (medical OR health) |
| Q08 | ("tool misuse" OR "excessive agency" OR "agent goal hijack") AND (healthcare OR medical OR clinical) |
| Q09 | taxonomy AND (attack OR threat) AND ("medical LLM" OR "clinical LLM" OR "healthcare AI agent") |
| Q10 | ("Delphi" OR "expert panel" OR "practitioner survey") AND ("AI agent" OR LLM) AND security |
| V01 | agent security AND healthcare (broad) |
| V02 | zero trust / guardrails for healthcare AI agents |
| V03 | MITRE ATLAS / STRIDE AND LLM AND healthcare |
| V04 | PHI leakage / privacy attacks on clinical LLM agents |
| V05 | MCP / tool poisoning / agent-to-agent AND health |
| V06 | adversarial attacks / jailbreak on medical LLM agents (EHR agents) |
| V07 | health insurance / claims AND LLM security (non-agent wording) |
| V08 | OWASP LLM Top 10 applied to healthcare |
| V09 | threat model / risk framework for LLM-integrated systems (domain-agnostic) |
| V10 | hospital / health system AI agent deployment security |

**Disconfirmation queries** (Semantic Scholar bulk search). These were built to find work
that would contradict the novelty claims:

| ID | Purpose (as logged) | Hits |
|---|---|---|
| D01 | OWASP agentic Top 10 applied to healthcare | 99 |
| D02 | payer / health plan agentic security | 122 |
| D03 | X12 / EDI / 278 / 837 with LLM | 300 kept (408 total) |
| D04 | fax / OCR / scanned medical records as LLM injection path | 13 |
| D05 | FHIR / HL7 / C-CDA as attack surface for LLM agents | 58 |
| D06 | prior authorization / utilization review AI risks (security) | 56 |
| D07 | follow-up: medical prompt-injection benchmarks | 56 |
| D08 | follow-up: author search for the authors of two starting-point papers | 0 |
| D09 | member service / contact center healthcare agent security | 14 |
| D10 | revenue cycle / claims adjudication LLM agent risks | 54 |
| D11 | threat model of healthcare agents by workflow (generic wording) | 39 |

**Other searches:**
- PM1 (PubMed): (prior authorization OR claims OR payer OR health plan) AND (LLM OR agent)
  AND (security OR injection OR attack). 4,172 records.
- SP1 to SP3: the IEEE *Security & Privacy* venue sweep (326 records, 41 passing the title
  filter).
- W01 to W05: web searches on the OWASP agentic list in healthcare, payer agent threats,
  and HL7, X12 or fax as injection carriers.
- Snowballing: backward and forward citations of 10 seed papers (274 records).
- A known-ID check of three named starting points, all of which exist.

## Screening

### Automated filters (before manual screening)

- **Pre-filter:** an LLM or agent term AND a security term in the title or abstract, AND a
  health term, or the OWASP agentic name together with an agent term.
- **Strict filter:** an explicit LLM term, a strong security term (privacy-only or generic
  wording failed) and a health term.
- **Spot check:** of the 2,527 records the filters excluded in Milestone 1, the 85 with both a
  health and a security term in the title were read. Two relevant payer papers were
  recovered (S58, S59), both framed around "privacy". Two further title-only records were
  logged as not retrieved.
- **Known weakness:** records with neither a health nor a security term in the title were not
  spot-checked. The residual miss rate is unknown, and payer work framed as "compliance" is
  the most likely blind spot. A third false negative (S69, a clinical-agent sandbox) was
  later recovered through PubMed.

### Inclusion and exclusion

No inclusion criterion is recorded as a single formal statement. The criteria below are
taken from the screening decisions and reasoning entries that applied them.

- **Included:** work that models or assesses security threats to LLM or agent systems in a
  healthcare context, or applies the OWASP agentic list in a structured way (R-13; the
  screening reason "meets inclusion rule").
- **Venue-sweep rule:** for IEEE *Security & Privacy* only, an agentic-AI security threat
  analysis in any sector (R-19). The author asked for these articles as venue references.
- **Grey literature:** the OWASP announcement page (the taxonomy itself), and one automated
  third-party audit page that flags X12 837 free text as an indirect-injection risk (G01).
  The audit page was added at the author's request and is labeled motivation only, not
  peer-reviewed (R-21).
- **Fact sources:** government rules, companion guides, standards pages, adversary-grounding
  pages and venue rules were logged as background used only for factual statements, not as
  research literature.
- **Excluded,** with the logged reasons:
  - healthcare AI work without a security-threat model of an LLM system (applications,
    architecture, governance, accuracy, general reviews);
  - LLMs or agents used as a security tool, not threats to LLM systems;
  - no healthcare context and no structured OWASP agentic use;
  - measurement or evaluation methodology (out of scope);
  - output-level, non-agentic jailbreak or refusal benchmarks;
  - vendor and consultancy material with no stated method (R-14).

### Counts

| Stage | Count |
|---|---|
| Milestone 1: unique records from database searches (31 queries) | 2,989 |
| Milestone 1: snowball records | 274 (31 duplicates) |
| Milestone 1: unique records in the screening log | 3,155 |
| Milestone 1: excluded by automated filters | 2,527 |
| Milestone 1: screened manually on title and abstract | 628 |
| Milestone 1: included | 50 papers + 1 framework page |
| After the pre-Milestone-2 additions (PubMed, venue sweep, re-screens, grey literature) | 7,716 screening rows; 61 papers + 2 web pages included |
| After Milestone 2 fact sources were added | 7,727 rows in the screening log; 74 source notes |

The novelty report gives 7,721 rows and 68 notes at the point where the four standards
pages were added. The screening log now holds six further fact-source rows: the X12
companion guides, the two federal rules, the two adversary-grounding pages and the venue
rules. That accounts for the difference.

Of the 61 included papers, 30 were read in full (3 of them through preprint versions) and 31
at abstract level only. All IEEE *Security & Privacy* articles were read at abstract level
only. Paywalled or blocked sources (SSRN, MDPI, Nature, Springer, JMIR, TechRxiv,
Preprints.org, IEEE, ACM, SciTePress) stayed abstract-only unless the author supplied a copy.
The author supplied the full texts of S03 and S06.

## Adjacent work considered and excluded

| Work (short) | Year | Stage | Reason recorded |
|---|---|---|---|
| Agentic AI for prior-authorization workflows (S40) | 2025 | Full text | Security appears only as compliance controls (HIPAA, RBAC); no threat analysis of the agent (R-13) |
| Agentic governance and adversarial verification for healthcare appeal generation (S56) | 2026 | Full text | "Adversarial verification" is an output-quality check for appeal letters; no attacker model (R-13) |
| Multi-agent framework for prior authorization with FHIR (preprint) | 2026 | Abstract (full text returned 403) | Prior-authorization automation with no security angle in the abstract; the full text was not read and might contain a security section (R-13) |
| OWASP Top 10 for LLM Applications (2023-2024 list) | — | Grey literature | Not the agentic list; background only (R-18) |
| Guardrails for insurance AI | 2025 | Abstract (spot check) | Property-and-casualty insurance, not health; hallucination guardrails |
| AI framework for security in medical research environments | 2026 | Abstract (spot check) | AI agents used as security tooling, not threats to agents |
| Comprehensive safety and adversarial-robustness benchmark for medical LLMs | 2025 | Abstract | Output-level refusal benchmark; non-agentic (R-18) |
| Holistic threat model for ML-based healthcare systems (HEALTHINF 2025), and a 2023 comparative framework | 2025, 2023 | Author lookup | Not LLM-specific (R-4) |
| Review of TRiSM frameworks in AI systems | 2026 | Title/abstract | No healthcare threat model; no structured OWASP agentic use |
| Red-teaming procedure for clinical decision-support LLMs | 2025 | Abstract | Evaluation procedure for non-agentic LLMs (measurement, out of scope) |
| Monitoring medical LLMs through verbalized reasoning | 2026 | Abstract | Monitoring method (measurement, out of scope); no threat model |
| Vulnerability of multi-agent medical systems to human interventions | 2026 | Abstract | Diagnostic robustness; no adversary model |
| LLM chart extraction for workers' compensation | 2026 | Abstract (PubMed) | Payer-adjacent but no security or threat content (R-20) |
| Vendor guides, consultancy articles and a personal developer blog (web searches W01, W04, W05) | — | Web | Opinion without a stated method, partly commercial. Logged as a counter-signal: practitioners know of payer agent risks informally (R-14) |

**Not retrieved** (no abstract, paywalled or blocked; content not described):
- From threat to trust: assessing security risks of agentic AI systems (2026: *International
  Journal of Information Security* 25(1), article 23, published online 4 Jan 2026). The year
  was checked on 2026-11-23 against the publisher's metadata record for DOI
  10.1007/s10207-025-01185-y at Crossref, because the paper itself could not be opened. The
  novelty report had given 2025.
- Prompt injection in clinical AI systems (2026);
- Clinically weighted zero trust for healthcare AI (2025);
- Secure multi-agent LLMs in healthcare: agent-in-the-middle attacks (2026);
- Word-level adversarial perturbations on EHR clinical text (2025).

## Known limits of the search

- Abstract-only reading of 31 included papers. All venue articles are among them.
- The automated filters have a known, non-zero false-negative rate (three known cases).
- Forward snowballing was weak, because most seeds were from 2026 and 6 of 10 had no indexed
  forward citations.
- Some gap-matrix values come from keyword counts, not sentence-level reading. These are
  marked "[keyword scan]" in the private notes.
- Per-query hit counts are in the private search log. This note gives them only for the
  disconfirmation queries.
