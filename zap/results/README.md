# ZAP Scan Results

## The two reports the dissertation actually reports on

- **`zap_unauth_report.html`** — the unauthenticated scan, generated
  **21 July 2026, 22:22**. Contains the SQL Injection alert on the OTP
  endpoint and the server-version-leak finding described in Dissertation
  Section 4.3.1. This is the file Table 3.2's "21 July 2026" date refers to.
- **`zap_auth_report.html`** — the authenticated scan, generated
  **6 August 2026, 22:33**. Contains the "Remote File Inclusion" alert on
  the mechanic-contact endpoint discussed in Section 4.3.2 (ZAP's
  misclassification of the SSRF finding, central to the Section 5.1
  sensitivity analysis).

## How these were identified

Multiple candidate files existed with similar names and overlapping dates.
They were disambiguated by checking which files actually contain the
specific alerts the dissertation describes (SQL Injection for the
unauthenticated scan; Remote File Inclusion for the authenticated scan),
rather than by filename or file-modification date alone, since `cp`/upload
operations can change a file's modified-time without changing its content.
Both files above were verified this way before being placed here.

## Files intentionally excluded from the main results

Two additional ZAP reports exist from the same testing period but do
**not** match the specific findings the dissertation describes, and are
kept separately in `exploratory-reruns/` rather than presented as primary
evidence:

- `zap_report_prelim_21jul.html` — generated 21 July 2026, 22:05, 17
  minutes before the real unauthenticated scan. Smaller scope (no SQL
  Injection alert), likely a preliminary/spider-only pass before the
  full API-driven scan.
- `zap_unauth_rerun_16aug.html` — a later unauthenticated re-run,
  16 August 2026. Also lacks the SQL Injection finding present in the
  original 21 July run — ZAP's active-scan payload ordering is
  non-deterministic between runs, so this is expected variation, not
  a contradiction. Kept for reference but not used as the study's
  reported result, since it doesn't match what Section 4.3.1 describes.

If you're extending this study and want to investigate scan-to-scan
variance in ZAP's findings, these two files plus the primary
`zap_unauth_report.html` give you three separate unauthenticated runs
against the same target to compare.
