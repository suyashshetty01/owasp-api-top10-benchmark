# Ground Truth - Nine Confirmed Vulnerabilities

Nine of the ten OWASP API Security Top 10 (2023) categories were manually
confirmed in OWASP crAPI using Burp Suite Repeater before automated tool
evaluation commenced. The tenth, API10 (Unsafe Consumption of APIs), has no
confirmed exploit in this study - see the note at the bottom of this file.


| ID | Category | Endpoint | Method | HTTP Result | Evidence |
|---|---|---|---|---|---|
| API1 | Broken Object Level Authorization | /identity/api/v2/vehicle/{vehicleId}/location | GET | 200 OK | Cross-user vehicleId substitution returned victim location |
| API2 | Broken Authentication | /identity/api/v2/vehicle/vehicles | GET | 200 OK | JWT token remained valid and accepted after logout |
| API3 | Broken Object Property Level Authorization | /identity/api/v2/user/videos/{id} | PUT | 200 OK | Hidden field `conversion_params` accepted via mass assignment |
| API4 | Unrestricted Resource Consumption | /community/api/v2/coupon/validate-coupon | POST | 200 OK | 10 rapid requests sent, no rate limiting (429) returned |
| API5 | Broken Function Level Authorization | /identity/api/v2/admin/videos/{id} | DELETE | 200 OK | Normal user's token accepted on an admin-only endpoint |
| API6 | Unrestricted Business Flows | /workshop/api/shop/orders/return_order | POST | 200 OK | QR refund issued without item-return verification |
| API7 | Server-Side Request Forgery | /workshop/api/merchant/contact_mechanic | POST | 200 OK | Server fetched an attacker-supplied external URL |
| API8 (finding 1) | Security Misconfiguration | /api-docs | GET | 200 OK | Swagger/OpenAPI UI accessible without authentication |
| API8 (finding 2) | Security Misconfiguration | /community/api/v2/coupon/validate-coupon | POST | 200 OK | NoSQL operator injection (`{"coupon_code": {"$ne": ""}}`) returned a valid coupon code (TRAC075) |
| API9 | Improper Inventory Management | /workshop/api/shop/orders/all | GET | 200 OK | Shadow endpoint returns all orders - not present in the OpenAPI spec |
| API10 | Unsafe Consumption of APIs | - | - | - | **No confirmed exploit.** See note below. |

## Why API10 has no confirmed exploit

crAPI's challenge set was built against the 2019 edition of the OWASP API
Top 10, in which the tenth category was *Insufficient Logging &
Monitoring*. That category was removed and replaced with an unrelated new
category, *Unsafe Consumption of APIs*, in the 2023 revision - a scenario
crAPI was never designed to exercise, since the category did not exist when
crAPI was built. See the dissertation, Section 3.3.1, for the full
reasoning with citations.

## API1 - BOLA - Test Detail

1. Authenticated as User A.
2. Called `GET /community/api/v2/community/posts/recent`.
3. Response exposed the `vehicleId` of another user (`robot001@example.com`).
4. Substituted that `vehicleId` into the vehicle location endpoint, using
   User A's own valid token.
5. Server returned HTTP 200 with the victim's private location, name, and
   email.
6. No ownership validation was performed - the server checked only that the
   token was valid, not that the requester owned the vehicle referenced.

## API2 - Broken Authentication - Test Detail

1. Logged in and obtained a valid JWT.
2. Called `POST /identity/api/auth/logout` (or equivalent) to end the
   session.
3. Re-sent the *same* JWT against `GET /identity/api/v2/vehicle/vehicles`.
4. Server returned HTTP 200 and valid data - the token was still accepted
   after logout, meaning session invalidation/token revocation was not
   enforced server-side.

## API3 - Broken Object Property Level Authorization - Test Detail

1. Called `PUT /identity/api/v2/user/videos/{id}` with the standard,
   documented request body.
2. Added an undocumented field, `conversion_params`, not present in the
   OpenAPI spec for this endpoint.
3. Server returned HTTP 200 and accepted the extra field - mass assignment:
   the endpoint bound the entire request body to an internal object rather
   than validating against an explicit allow-list of writable properties.

## API4 - Unrestricted Resource Consumption - Test Detail

1. Sent 10 rapid, back-to-back requests to
   `POST /community/api/v2/coupon/validate-coupon`.
2. All 10 returned normal application responses (HTTP 200).
3. No HTTP 429 (Too Many Requests) or other rate-limiting response was ever
   returned, indicating no request-volume protection on this endpoint.

## API5 - Broken Function Level Authorization - Test Detail

1. Authenticated as a standard (non-admin) user, obtaining a valid JWT.
2. Called `DELETE /identity/api/v2/admin/videos/{id}`, an endpoint intended
   for admin-role users only.
3. Server returned HTTP 200 and performed the deletion - the standard
   user's token was accepted on an admin-only function, indicating the
   endpoint checks only for a valid token, not for the caller's role.

## API6 - Unrestricted Business Flows - Test Detail

1. Purchased an item via the crAPI Shop.
2. Called `POST /workshop/api/shop/orders/return_order` directly via Burp
   Repeater, without going through any UI-enforced return process.
3. Server returned HTTP 200 with a refund QR code immediately.
4. No physical-return verification, cooldown period, or multi-step
   confirmation was required - a full refund was obtained without ever
   returning the item.

## API7 - SSRF - Test Detail

1. Called `POST /workshop/api/merchant/contact_mechanic` with an
   attacker-controlled URL placed in the `mechanic_api` field.
2. Server returned HTTP 200 and made an outbound request to that
   attacker-supplied URL - confirmed via the receiving server's own access
   log.
3. No allow-list or validation was applied to the destination host before
   the server-side request was made.

## API8 (finding 1) - Security Misconfiguration - Test Detail

1. Requested `GET /api-docs` without any authentication token.
2. Server returned HTTP 200 with the full Swagger/OpenAPI UI and
   specification, exposing the complete API surface (including
   undocumented-elsewhere endpoint details) to unauthenticated clients.

## API8 (finding 2) - Security Misconfiguration - Test Detail

1. Sent the payload `{"coupon_code": {"$ne": ""}}` to
   `POST /community/api/v2/coupon/validate-coupon`, in place of a normal
   string coupon code.
2. Server returned HTTP 200 with a real, valid coupon code (`TRAC075`,
   worth $75).
3. The server passed the input directly to a MongoDB query without type
   validation, allowing the `$ne` (not-equal) operator to match any
   non-empty value and bypass the coupon check entirely.

## API9 - Improper Inventory Management - Test Detail

1. Endpoint `GET /workshop/api/shop/orders/all` was found to exist and
   return data, despite not appearing anywhere in the published OpenAPI
   specification or being linked from the crAPI UI.
2. Server returned HTTP 200 with all orders across all users - a shadow
   endpoint invisible to specification-driven discovery, only found through
   manual exploration.
