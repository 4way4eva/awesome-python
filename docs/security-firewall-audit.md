# Firewall, Defense Security, and Audit Configuration

This project now includes a concrete baseline for **defensive controls** and **auditability**.

## Objectives

- Enforce a default-deny network policy.
- Allow only explicit, minimal ingress/egress paths.
- Capture auditable security events across identity, config, data, and runtime.
- Preserve integrity of logs for incident response and legal/compliance workflows.

## Firewall baseline

Defined in `configs/security/firewall.yaml`:

- `default_policy` denies inbound, outbound, and east-west traffic by default.
- Controlled exceptions are defined as explicit allow rules with:
  - stable rule IDs,
  - protocol and port constraints,
  - source/destination tags or CIDRs,
  - human-readable justification.
- Additional controls include anti-spoofing, rate-limiting, and IDS/IPS enablement.

## Audit baseline

Defined in `configs/security/audit.yaml`:

- Required audit scopes:
  - authentication events,
  - configuration changes,
  - data access and export events,
  - runtime process/network indicators.
- Retention model includes hot/warm/cold windows and immutable storage.
- Integrity controls enforce log signing, hash chaining, and tamper alerts.
- SIEM alert thresholds and responders are predeclared.

## Validation workflow

Run local validation:

```bash
python scripts/validate_security_config.py
```

Run via make:

```bash
make security_audit
```

## Operational notes

- Keep defaults deny-first; add exceptions only via ticketed change management.
- Review rule usage monthly and remove stale exceptions.
- Couple alert thresholds to incident response SLAs.
