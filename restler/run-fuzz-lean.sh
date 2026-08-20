#!/usr/bin/env bash
# RESTler fuzz-lean run against crAPI, using grammar_final.py
# Reconstructed from Dissertation Section 4.4 and Figure 4.6.
#
# KNOWN ISSUE (documented in the dissertation as the central RESTler finding):
# on an ARM64 host running this image via x86 emulation, RESTler's
# token_refresh_command does not reliably inject the JWT into outbound
# requests, causing the ResourceHierarchyChecker (the BOLA-relevant checker)
# to never activate. See Dissertation Section 4.4 for the full diagnosis.
# Running this on a native x86 Linux host is the recommended next step
# (Section 6.3) to determine whether the issue is emulation-specific.

set -euo pipefail

# TODO: confirm token.txt generation method against your original session —
# this assumes a JWT was written to a local token.txt file and refreshed via
# `cat`, matching the token_refresh_command shown in Figure 4.6.
docker run --network docker_default \
  -v "$(pwd)":/restler/workdir \
  mcr.microsoft.com/restlerfuzzer/restler \
  compile \
  --api_spec /restler/workdir/Compile/crapi-spec.json

docker run --network docker_default \
  -v "$(pwd)":/restler/workdir \
  mcr.microsoft.com/restlerfuzzer/restler \
  fuzz-lean \
  --grammar_file /restler/workdir/Compile/grammar_final.py \
  --dictionary_file /restler/workdir/Compile/dict.json \
  --settings /restler/workdir/Compile/engine_settings.json \
  --no_ssl \
  --target_ip crapi-web \
  --target_port 80 \
  --host crapi-web \
  --token_refresh_interval 99999 \
  --token_refresh_command "cat /restler/workdir/token.txt"
