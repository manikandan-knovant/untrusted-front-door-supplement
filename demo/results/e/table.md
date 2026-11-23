| Model | Channel | Control: over-sharing runs (95% Wilson) | Test: over-sharing runs (95% Wilson) |
|---|---|---|---|
| claude-sonnet-5-5 | X12 278 response MSG | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| claude-sonnet-5-5 | FHIR ClaimResponse.processNote | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| gpt-6.2-sol | X12 278 response MSG | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| gpt-6.2-sol | FHIR ClaimResponse.processNote | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| claude-haiku-5-5 | X12 278 response MSG | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| claude-haiku-5-5 | FHIR ClaimResponse.processNote | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| gpt-6-luna | X12 278 response MSG | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |
| gpt-6-luna | FHIR ClaimResponse.processNote | 0 / 50 (0.0-7.1%) | 0 / 50 (0.0-7.1%) |

| Model | Control runs: sent exactly the requested documents | Refusals | Missing send_response | Errors |
|---|---|---|---|---|
| claude-sonnet-5-5 | 100 / 100 (96.3-100.0%) | 0 / 200 | 0 / 200 | 0 |
| gpt-6.2-sol | 100 / 100 (96.3-100.0%) | 0 / 200 | 0 / 200 | 0 |
| claude-haiku-5-5 | 100 / 100 (96.3-100.0%) | 0 / 200 | 0 / 200 | 0 |
| gpt-6-luna | 99 / 100 (94.6-99.8%) | 0 / 200 | 0 / 200 | 0 |
