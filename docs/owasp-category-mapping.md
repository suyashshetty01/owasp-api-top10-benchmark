# OWASP API Top 10 (2023) Category Mapping

Reproduced from Dissertation Table 3.1. Documents which confirmed exploit
maps to which OWASP category, and the source justifying each assignment.

| ID | Vulnerability confirmed | OWASP category | Source for mapping |
|---|---|---|---|
| API1 | Vehicle location disclosed via another user's vehicleId | Broken Object Level Authorization | crAPI challenge guide, Vehicle service |
| API2 | OTP/authentication flow weaknesses | Broken Authentication | crAPI challenge guide, Identity service |
| API3 | Excessive property exposure / mass assignment | Broken Object Property Level Authorization | crAPI challenge guide, Shop/Profile modules |
| API4 | Unrestricted resource consumption | Unrestricted Resource Consumption | crAPI challenge guide |
| API5 | Function-level authorization bypass | Broken Function Level Authorization | crAPI challenge guide |
| API6 | Refund issued without physical return verification | Unrestricted Business Flows | crAPI challenge guide, Return-order flow |
| API7 | SSRF via mechanic_api field | Server-Side Request Forgery | crAPI challenge guide, Workshop service |
| API8 | Coupon validation bypass via NoSQL operator injection ($ne) | Security Misconfiguration (reassigned from API10 - see note below) | crAPI challenge guide, Coupon endpoint |
| API9 | Undocumented shadow endpoint (/shop/orders/all) | Improper Inventory Management | crAPI challenge guide |
| API10 | - no confirmed exploit in this study | Unsafe Consumption of APIs | OWASP (2023a) category definition |

## Why API10 has no confirmed exploit

crAPI's challenge set was built against the **2019** edition of the OWASP
API Security Top 10, in which the tenth category was *Insufficient Logging
& Monitoring*. That category was removed entirely in the 2023 revision and
replaced with an unrelated new category, *Unsafe Consumption of APIs* -
which OWASP (2023a) defines around risks from consuming untrusted
third-party API responses. This scenario did not exist as a category when
crAPI was designed, so crAPI's challenge set was never built to exercise it.

This is a taxonomy-alignment gap between the test environment's vintage and
the framework version selected for this study - see Dissertation Section
3.3.1 for the full reasoning, with citations.

