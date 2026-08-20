# Publishing Checklist

## Done

- [x] `restler/grammar_clean.py` - real file, verified valid Python, scanned for secrets.
- [x] `restler/grammar_final.py` - real file, verified valid Python, scanned for secrets.
- [x] `environment/crapi-version.md` - pinned to commit `73d309cc8f28bbdeed31dbb35f05dba8354de3c9`, plus all 7 Docker image digests.
- [x] `restler/results/testing_summary_run1.json` - real file (`~/restler-work/FuzzLean/RestlerResults/experiment34/logs/testing_summary.json`).
- [x] `zap/results/zap_unauth_report.html` and `zap_auth_report.html` - real files, verified by content (not just filename/date) to be the actual scans the dissertation reports on. See `zap/results/README.md` for how these were disambiguated from three other similarly-named candidate files.

## Known limitation, accepted rather than fixed

- [ ] `restler/results/testing_summary_run2.json` remains a **reconstruction**
      from a screenshot, not the original file. The real second-run summary
      (grammar_final.py, 1/41 coverage) was not separately saved - only one
      experiment folder (`experiment34`) exists under `FuzzLean/RestlerResults/`,
      and it currently holds the first run's data. This is disclosed via the
      `_provenance_note` field inside the JSON file itself.

## Should do (strengthens the artefact, not blocking)

- [ ] A LICENCE file - MIT is a reasonable default; see README.
- [ ] A CITATION file or a line in the dissertation's reference list pointing
      to this repo's URL, once it's live.
- [ ] Confirm the full ZAP authenticated-scan replacer config against your
      shell history (`history | grep zap-api-scan`) - the version in
      `zap-authenticated-scan.sh` is reconstructed from a partially-cropped
      screenshot and marked `TODO` where uncertain.
- [ ] Consider whether the "Format String Error" alert found in
      `zap_auth_report.html` (not currently discussed in the dissertation)
      is worth a mention in Section 4.3 - it's a real finding in your data
      that isn't yet written up.

## Security - do not skip

- [ ] Before your first commit, run one more check yourself:
      `git grep -i "eyJ"` (catches most JWTs). This session's own checks
      found the repo clean, but it's good practice to verify independently
      before pushing.
- [ ] Consider rotating your crAPI test-account credentials, since this
      session involved pasting a real JWT into a chat conversation at one
      point - that token should not be reused going forward.

## Optional polish

- [ ] Add a GitHub Actions workflow that re-runs the ZAP scans periodically,
      demonstrating the "reproducible Docker-based methodology" claim stays
      true over time.
- [ ] Investigate the scan-to-scan variance visible across your three
      unauthenticated ZAP runs (`zap_unauth_report.html` plus the two files
      in `exploratory-reruns/`) - the SQL Injection finding only appeared
      in the original 21 July run, which is a genuine, mentionable
      observation about ZAP's non-determinism if you want to strengthen
      Section 3.6's limitations discussion.
