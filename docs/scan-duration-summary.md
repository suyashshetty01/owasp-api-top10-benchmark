# Scan Duration and Request Summary

Reproduced from Dissertation Table 3.2. Durations were reconstructed from
run logs after the fact and were **not equalised** across tools - each tool
ran to its own natural completion or failure point rather than a shared time
or request budget. This non-equalisation is a stated limitation (Dissertation
Section 3.4, Section 6.3), not something this table resolves.

| Tool / configuration | Date | Duration | Requests / URLs | Comparable to other rows? |
|---|---|---|---|---|
| Burp Suite – manual (Repeater) | July 2026 | ~4 hours (manual testing) | Manual only - not applicable | No - not a scan; ground-truth instrument only |
| ZAP – unauthenticated | 21 July 2026 | ~12 minutes | 197 URLs tested | Yes, to ZAP-authenticated |
| ZAP – authenticated (JWT) | 6 August 2026 | ~33 minutes | 198 URLs tested | Yes, to ZAP-unauthenticated |
| RESTler – fuzz-lean | 6 August 2026 | ~2 minutes | 214 requests (main driver, first run) | No - dependency chain failed before full coverage; see Section 4.4 |

## Why RESTler's short duration is not a sign of efficiency

RESTler's ~2-minute run is roughly 16x shorter than ZAP's authenticated
33-minute run. This reflects the dependency chain failing early - not the
tool completing a thorough pass. This is consistent with RESTler achieving
only 2/41 endpoints of valid coverage (see
`../restler/results/testing_summary_run1.json`).

A meaningfully equalised comparison would require either capping ZAP's
authenticated run to RESTler's ~2-minute window (which would almost
certainly reduce ZAP's own coverage well below 198 URLs), or extending
RESTler's run to ZAP's ~33-minute window - not achievable while RESTler's
token-injection failure prevents it from building request sequences past
its current dependency-chain ceiling, regardless of how long it runs. Real,
unequal durations are reported here rather than a synthetic equalised
figure.
