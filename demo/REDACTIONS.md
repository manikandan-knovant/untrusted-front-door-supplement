# Redactions

Eight documents in `demo/` are published as redacted copies. Three kinds of text were replaced;
no other character was changed.

| Kind | Marker | Rule |
|---|---|---|
| Planted sentence | `[PLANTED SENTENCE WITHHELD - see REDACTIONS.md, item N]` | The text matched a sentence planted in test packets in full, or contained a run of 8 or more consecutive words from one (case and punctuation ignored). Every match found was a full sentence. |
| Payload note wording | `[PAYLOAD NOTE WORDING WITHHELD - see REDACTIONS.md, item N]` | The text contained a run of 8 or more consecutive words from the description note stored with the planted sentences. These runs are partly made of short planted-sentence fragments. |
| Absolute local path | `[local path removed]` | A file path on the author's computer that contained the author's user name. |

No redacted text is given here.

The studies used four distinct planted sentences, labelled S1 to S4. Items with the same label
replace the same sentence. Planted sentences appear only in test-condition packets; control
packets have none. N1 to N3 are the description notes stored with them; the notes were never
placed in any packet.

| Label | Used in |
|---|---|
| S1 | Study A, test condition (channel x12_837_nte) |
| S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| S3 | Studies C and D, test condition; study F, claims task, test condition |
| S4 | Study E, test condition; study F, records task, test condition |
| N1 | Note stored with S1 and S2 (studies A and B) |
| N2 | Note stored with S3 (studies C, D, and F claims task) |
| N3 | Note stored with S4 (studies E, and F records task) |

| Item | File | Line | Kind | Label | Study and condition |
|---|---|---|---|---|---|
| 1 | `demo/PREREG_B.md` | 64 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 2 | `demo/PREREG_E.md` | 106 | planted sentence | S4 | Study E, test condition; study F, records task, test condition |
| 3 | `demo/PREREG_F.md` | 36 | planted sentence | S4 | Study E, test condition; study F, records task, test condition |
| 4 | `demo/TEST_STRATEGY_REVIEW.md` | 98 | planted sentence | S1 | Study A, test condition (channel x12_837_nte) |
| 5 | `demo/TEST_STRATEGY_REVIEW.md` | 99 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 6 | `demo/TEST_STRATEGY_REVIEW.md` | 167 | planted sentence | S1 | Study A, test condition (channel x12_837_nte) |
| 7 | `demo/TEST_STRATEGY_REVIEW.md` | 233 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 8 | `demo/TEST_STRATEGY_REVIEW.md` | 305 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 9 | `demo/TEST_STRATEGY_REVIEW.md` | 469 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 10 | `demo/TEST_STRATEGY_REVIEW.md` | 553 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 11 | `demo/TEST_STRATEGY_REVIEW.md` | 703 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 12 | `demo/TEST_STRATEGY_REVIEW.md` | 876 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 13 | `demo/TEST_STRATEGY_REVIEW.md` | 966 | planted sentence | S2 | Studies A and B, test condition (A: ccda_275, x12_271_msg, fhir_supportinginfo, fax_ocr; B: ccda_275, fhir_supportinginfo, fax_ocr) |
| 14 | `demo/TEST_STRATEGY_REVIEW.md` | 1003 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 15 | `demo/TEST_STRATEGY_REVIEW.md` | 1075 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 16 | `demo/TEST_STRATEGY_REVIEW.md` | 1248 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 17 | `demo/TEST_STRATEGY_REVIEW.md` | 1338 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 18 | `demo/TEST_STRATEGY_REVIEW.md` | 1479 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 19 | `demo/TEST_STRATEGY_REVIEW.md` | 1551 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 20 | `demo/TEST_STRATEGY_REVIEW.md` | 1618 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 21 | `demo/TEST_STRATEGY_REVIEW.md` | 1655 | planted sentence | S3 | Studies C and D, test condition; study F, claims task, test condition |
| 22 | `demo/reasoning_demo.md` | 79 | planted sentence | S1 | Study A, test condition (channel x12_837_nte) |
| 23 | `demo/DESIGN.md` | 41 | payload note wording | N1 | Note stored with sentences S1 and S2 (studies A and B); not part of any packet |
| 24 | `demo/PREREG_C.md` | 42 | payload note wording | N2 | Note stored with sentence S3 (studies C, D and F claims); not part of any packet |
| 25 | `demo/PREREG_D.md` | 21 | payload note wording | N2 | Note stored with sentence S3 (studies C, D and F claims); not part of any packet |
| 26 | `demo/PREREG_E.md` | 23 | payload note wording | N3 | Note stored with sentence S4 (studies E and F records); not part of any packet |
| 27 | `demo/PREREG_F.md` | 35 | payload note wording | N2 | Note stored with sentence S3 (studies C, D and F claims); not part of any packet |
| 28 | `demo/reasoning_demo.md` | 74 | payload note wording | N1 | Note stored with sentences S1 and S2 (studies A and B); not part of any packet |
| 29 | `demo/reasoning_demo.md` | 164 | payload note wording | N2 | Note stored with sentence S3 (studies C, D and F claims); not part of any packet |
| 30 | `demo/reasoning_demo.md` | 455 | payload note wording | N3 | Note stored with sentence S4 (studies E and F records); not part of any packet |
| 31 | `demo/TEST_STRATEGY_REVIEW.md` | 1948 | absolute local path | - | Not study material: a local file path containing the author's user name |

Items per file: `DESIGN.md` 1, `PREREG_B.md` 1, `PREREG_C.md` 1, `PREREG_D.md` 1, `PREREG_E.md` 2, `PREREG_F.md` 2, `TEST_STRATEGY_REVIEW.md` 19, `reasoning_demo.md` 4; 31 in total.

The unredacted originals are kept privately by the author. Their SHA-256 hashes are in
[`ORIGINAL_HASHES.txt`](ORIGINAL_HASHES.txt).
