#!/usr/bin/env bash
# ZAP unauthenticated scan against crAPI
# Reconstructed from the invocation shown in Dissertation Figure 4.1.
# Ran: 21 July 2026, ~12 minutes, 197 URLs tested (Table 3.2).
#
# Prerequisites: crAPI running and reachable at http://crapi-web on the
# docker_default network; crapi-spec.json (the OpenAPI spec) present in the
# current working directory.

set -euo pipefail

docker run --network docker_default \
  -v "$(pwd)":/zap/wrk \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-api-scan.py \
  -t /zap/wrk/crapi-spec.json \
  -f openapi \
  -O http://crapi-web \
  -r zap_unauth_report.html
