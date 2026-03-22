# awesome-python (hardened docs profile)

This repository includes a minimal docs site plus security baseline artifacts for:

- perimeter/network firewall policy (default-deny posture)
- host/container egress controls
- audit logging, retention, and integrity requirements
- repeatable configuration validation in CI/local runs

## Quick start

```bash
pip install -r requirements.txt
make site_build
make security_audit
```

## Security artifacts

- `configs/security/firewall.yaml`
- `configs/security/audit.yaml`
- `scripts/validate_security_config.py`
- `docs/security-firewall-audit.md`

## Documentation site

Build static site:

```bash
make site_build
```

Serve locally:

```bash
make site_preview
```


## CODEXX

- Demo script: `scripts/codexx_demo.py`
- Doc page: `docs/codexx-demo.md`


## EV0LClock + Formal Audit

- Research brief: `docs/evolclock-deep-research.md`
- Formal edition: `docs/formal-edition-audit.md`
- Audit script: `scripts/codex_formal_audit.py`


## Additional analysis

- Arabic symbolic analysis: `docs/codex-scroll-ds-baba-ar.md`

- BLEU Day holiday system: `docs/bleu-day-of-thanks.md`

- EV0L decoded insights: `docs/evol-codex-decoded-insights.md`
