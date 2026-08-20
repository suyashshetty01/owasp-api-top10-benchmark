# crAPI Version Pinned for This Study

**Confirmed and pinned.**

- **Source**: official OWASP repository - `https://github.com/OWASP/crAPI`
- **Commit**: `73d309cc8f28bbdeed31dbb35f05dba8354de3c9`
- **Commit date**: 2026-05-15
- **Commit message**: "Fix version mismatch" (worth noting - this commit message
  itself suggests a known version-alignment issue was fixed around this
  time upstream; not investigated further, but flagged here in case it's
  relevant to a future reader trying to reconcile behaviour against a
  different crAPI commit).

## Docker image digests (all built 2025-09-22, consistent single deployment)

| Image | SHA256 digest |
|---|---|
| crapi/crapi-web | `b27d246c646bd33898e7d1d2095b6e7576c0993a7b81a73aa7386929493d7151` |
| crapi/crapi-identity | `5d1db5b3ba8e02bc68711ec6fc4e35ed7cd8b87e63785ece9e7ff5b5e36c5260` |
| crapi/crapi-community | `8ba0c7eda86ae065a673f1fa554d0109a24f25c5a8d65097ae024e5ee715c54e` |
| crapi/crapi-workshop | `d4d2d94d35a31e211b04d5a771881f5ae13e358e8fa0804463ae3bace05dd815` |
| crapi/crapi-chatbot | `36d274d54182a8baddba7ede17282035bb43ab9cb9cf87927e1fe7109901e0aa` |
| crapi/gateway-service | `97dade9daf0e758547b1686e2d3303c8c9b79838167f728a9211f0ee1f4622b0` |
| crapi/mailhog | `015c23f79d40c9dc1800cd0a458503b89aeda3b585a12c37d53829d6c7d61fdd` |

To reproduce exactly:

```bash
git clone https://github.com/OWASP/crAPI
cd crAPI
git checkout 73d309cc8f28bbdeed31dbb35f05dba8354de3c9
cd deploy/docker
docker compose pull
docker compose -f docker-compose.yml --compatibility up -d
```

## Deployment method used in this study

Per Section 3.2 of the dissertation:

- Deployed via Docker Compose on a local macOS (Apple Silicon / ARM64) host.
- Isolated Docker network (`docker_default`), no external network exposure.
- Standard crAPI microservices: identity, community, workshop, chatbot,
  gateway-service, mailhog; backed by PostgreSQL and MongoDB.
