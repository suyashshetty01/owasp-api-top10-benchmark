#!/usr/bin/env bash
# ZAP authenticated scan against crAPI (JWT injected via ZAP's replacer config)
# Partially reconstructed from the invocation shown in Dissertation Figure 4.3.
# Ran: 6 August 2026, ~33 minutes, 198 URLs tested (Table 3.2).
#
# TODO — the -z replacer config string below is INCOMPLETE. Figure 4.3 only
# shows the first few replacer options (description, enabled, matchtype,
# matchstr, regex, replacement=Bearer ...) before the terminal window cropped
# it off. Confirm the exact, full -z string against your own shell history:
#
#   history | grep -i "zap-api-scan"
#
# and replace the placeholder block below. DO NOT put a real JWT value in
# this file if you commit it — use the $JWT_TOKEN environment variable
# pattern shown here instead, so the actual token never touches source control.

set -euo pipefail

if [ -z "${JWT_TOKEN:-}" ]; then
  echo "Set JWT_TOKEN before running, e.g.:"
  echo "  export JWT_TOKEN=\"eyJhbGc...<your real token, obtained via crAPI login>\""
  exit 1
fi

# TODO: confirm this replacer config against your original command in full —
# only the first several -config flags are confirmed from the report's figures.
docker run --network docker_default \
  -v "$(pwd)":/zap/wrk \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-api-scan.py \
  -t /zap/wrk/crapi-spec.json \
  -f openapi \
  -O http://crapi-web \
  -z "-config replacer.full_list(0).description=auth \
      -config replacer.full_list(0).enabled=true \
      -config replacer.full_list(0).matchtype=REQ_HEADER \
      -config replacer.full_list(0).matchstr=Authorization \
      -config replacer.full_list(0).regex=false \
      -config replacer.full_list(0).replacement=Bearer\ ${JWT_TOKEN}" \
  -r zap_auth_report.html
