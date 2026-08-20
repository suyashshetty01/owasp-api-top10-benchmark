# OWASP API Top 10 - Automated Tool Benchmark

**Student:** Suyash Shetty | A00047320 | TU Dublin

## Overview

Comparative benchmark of three automated REST API security testing tools -
Burp Suite Community Edition (used as the manual ground-truth instrument),
OWASP ZAP 2.17.0, and RESTler 9.x - against the OWASP API Security Top 10
(2023) taxonomy, using OWASP crAPI as the test environment. Nine of the ten
taxonomy categories were manually confirmed as exploitable before any
automated tool was run; the tenth, API10, has no confirmed exploit in this
study - see `ground-truth/ground_truth.md` for why.

## Key Finding

Under the strict coding scheme, zero vulnerabilities were autonomously and
completely (TP) detected by ZAP, the only tool that completed a valid scan.
The best-performing configuration (ZAP, authenticated) produced three
partial detections (API2, API7, API8) out of nine confirmed categories. An
alternative coding of one SSRF alert changes this to one TP - see the
dissertation, Section 5.1, for why the headline number depends on that
single coding decision and is stated explicitly rather than left implicit.
API1 (BOLA) and API6 (Business Logic) were missed by every tool in every
configuration that completed a valid run.

## Detection Coverage Matrix

RESTler is marked **NVT** (Not Validly Tested) rather than FN wherever its
checkers did not execute - its dependency chain failed before reaching most
endpoints due to a JWT token-injection incompatibility on ARM64 (see
`restler/README.md`). This is a deployment failure, not a negative
detection result, and the two are not conflated in this table.

| ID | Category | Burp (manual instrument) | ZAP Unauth | ZAP Auth | RESTler |
|---|---|---|---|---|---|
| API1 | Broken Object Level Authorization | n/a – ground truth | FN | FN | NVT |
| API2 | Broken Authentication | n/a – ground truth | Partial | Partial | NVT |
| API3 | Object Property Level Auth | n/a – ground truth | FN | FN | NVT |
| API4 | Unrestricted Resource Consumption | n/a – ground truth | FN | FN | NVT |
| API5 | Broken Function Level Auth | n/a – ground truth | FN | FN | NVT |
| API6 | Unrestricted Business Flows | n/a – ground truth | FN | FN | NVT |
| API7 | Server-Side Request Forgery | n/a – ground truth | FN | Partial | NVT |
| API8 | Security Misconfiguration (incl. coupon NoSQL injection - reassigned from API10) | n/a – ground truth | Partial | Partial | NVT / Partial (bug found, not category-mapped) |
| API9 | Improper Inventory Management | n/a – ground truth | FN | FN | NVT |
| API10 | Unsafe Consumption of APIs | No confirmed exploit | Not scored | Not scored | Not scored |

Burp Suite Community Edition does not include Burp Scanner (that's a
Professional-tier feature), so it is not scored here as an automated
detector - it was used exclusively to manually confirm the nine ground-truth
vulnerabilities via Repeater.

## Tools Evaluated

| Tool | Version | Role in this study |
|---|---|---|
| Burp Suite Community | 2024.x | Manual ground-truth instrument (Repeater) - not an automated scanner |
| OWASP ZAP | 2.17.0 | Automated DAST, unauthenticated and authenticated configurations |
| RESTler | 9.x | Stateful fuzzing, fuzz-lean mode, seed=12345 - deployment-barrier case study, see `restler/README.md` |

## Repository Structure

- `ground-truth/` - nine confirmed vulnerabilities with endpoints and evidence (API10 excluded - see note in that folder)
- `zap/` - OpenAPI spec, ZAP scan commands, real scan reports
- `restler/` - grammar files, dictionary, engine settings, real results
- `docs/` - detection coverage matrix and scan duration summary, reproduced from the dissertation

## Why API10 has no confirmed exploit

crAPI's challenge set was built against the 2019 edition of the OWASP API
Top 10, where the tenth category was *Insufficient Logging & Monitoring*.
That category was removed and replaced with an unrelated new category,
*Unsafe Consumption of APIs*, in the 2023 revision - a scenario crAPI was
never designed to exercise, since the category did not exist when crAPI was
built. See `ground-truth/ground_truth.md` for the full reasoning.

## Environment

- crAPI, official OWASP repository, commit `73d309cc8f28bbdeed31dbb35f05dba8354de3c9` (2026-05-15)
- Deployed via Docker Compose on macOS (Apple Silicon / ARM64), isolated `docker_default` network

## Citation

Shetty, S. (2026) *Security Analysis of REST APIs using OWASP API Top 10:
A Comparative Benchmark Evaluation of Automated Security Testing Tools*.
MSc Thesis, TU Dublin.
