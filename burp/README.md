# Burp Suite Community Edition — No Automated Artefact

There is nothing to publish in this folder, and that's a deliberate finding,
not an oversight — see Section 4.2 of the dissertation.

Burp Suite Community Edition does not include Burp Scanner (PortSwigger's
active/passive detection engine); that's a Professional-tier feature. This
study used Burp CE exclusively as a **manual testing instrument** — Burp
Repeater — to hand-craft the requests that established the nine confirmed
ground-truth vulnerabilities documented in Section 4.2.1 of the dissertation.

There is no scan output, report file, or automated result to archive here,
because no automated scan was ever run with Burp in this study. If you're
looking for the actual exploitation evidence, it's in the dissertation itself
(Section 4.2.1) and in this repo's `docs/detection-coverage-matrix.md`.

If you want to reproduce the manual testing: install Burp Suite Community
Edition, configure it as an intercepting proxy in front of your crAPI
instance, and use Repeater to replay the requests described in Section 4.2.1
of the dissertation (e.g. substituting another user's `vehicleId` into the
vehicle location endpoint).
