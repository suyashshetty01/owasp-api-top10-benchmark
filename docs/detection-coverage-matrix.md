# Detection Coverage Matrix

Reproduced from Dissertation Table 4.1. RESTler is marked **NVT** (Not
Validly Tested) rather than FN wherever its checkers did not execute — see
Dissertation Section 4.4. API10 has no confirmed ground-truth exploit in
this study and is excluded from TP/FN/Partial scoring across all tools —
see Dissertation Section 3.3.1.

| ID | Category | Burp (manual instrument) | ZAP Unauth | ZAP Auth | RESTler |
|---|---|---|---|---|---|
| API1 | Broken Object Level Authorization | n/a – ground truth | FN | FN | NVT |
| API2 | Broken Authentication | n/a – ground truth | Partial | Partial | NVT |
| API3 | Object Property Level Auth | n/a – ground truth | FN | FN | NVT |
| API4 | Unrestricted Resource Consumption | n/a – ground truth | FN | FN | NVT |
| API5 | Broken Function Level Auth | n/a – ground truth | FN | FN | NVT |
| API6 | Unrestricted Business Flows | n/a – ground truth | FN | FN | NVT |
| API7 | Server-Side Request Forgery | n/a – ground truth | FN | Partial | NVT |
| API8 | Security Misconfiguration (incl. coupon NoSQL injection – reassigned from API10, see 3.3.1) | n/a – ground truth | Partial | Partial | NVT / Partial (bug found, not category-mapped – see 4.4) |
| API9 | Improper Inventory Management | n/a – ground truth | FN | FN | NVT |
| API10 | Unsafe Consumption of APIs | No confirmed exploit — see 3.3.1 | Not scored (no ground truth) | Not scored (no ground truth) | Not scored (no ground truth) |

## Legend

- **TP** — True Positive: tool autonomously detected and correctly categorised the vulnerability.
- **FN** — False Negative: vulnerability confirmed in ground truth, tool did not detect it.
- **Partial** — tool flagged related anomalous behaviour but did not correctly identify the core vulnerability.
- **NVT** — Not Validly Tested: the relevant checker did not execute due to a deployment failure (RESTler only — see Section 4.4). Distinct from FN: the checker did not look and fail to find the vulnerability, it did not look at all.
- **Not scored** — no ground-truth exploit exists in this study for this category (API10 only — see Section 3.3.1).

## Detection rate calculations (Table 4.3)

| Configuration | TP | TP+Partial | TP rate (of 9) | TP+Partial rate (of 9) | Noise ratio |
|---|---|---|---|---|---|
| ZAP – unauthenticated | 0 | 2 (API2, API8) | 0% | 22% | 78% (7/9 alerts unrelated) |
| ZAP – authenticated, strict coding | 0 | 3 (API2, API7, API8) | 0% | 33% | 75% (9/12 alerts unrelated) |
| ZAP – authenticated, TP-with-misclassification coding | 1 (API7) | 3 (API2, API7, API8) | 11% | 33% | 75% (unchanged) |

Note: scoring the unauthenticated scan against all nine confirmed categories
is arguably unfair to the tool — most of crAPI's surface returned HTTP 401
without a token, so the unauthenticated run never had genuine opportunity to
reach most endpoints. The 22% figure is a floor, not a fair like-for-like
measurement — see Dissertation Section 4.6.
