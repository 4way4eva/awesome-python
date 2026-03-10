# Security Deployment Package

## Objective
Provide a practical, deployable baseline for firewall defense and security audit configuration alongside site build output.

## Included controls
1. **Firewall baseline** (`security/firewall/iptables.rules.v4`)
   - Default deny for inbound/forward traffic
   - Explicit allowlist for SSH (22), HTTP (80), HTTPS (443)
   - Logging for denied packets
2. **Web security headers** (`security/nginx/security_headers.conf`)
   - CSP, frame protection, MIME sniff protection, and policy headers
3. **Audit rules** (`security/audit/auditd.rules`)
   - Watches identity, privilege, SSH, NGINX, and webroot paths
   - Logs root command execution events
4. **Automated baseline check** (`scripts/validate_security_baseline.py`)
   - Validates all required files and key hardening directives

## Build + validation flow
```bash
pip install -r requirements.txt
make site_build
python scripts/validate_security_baseline.py
```

## Notes
- These files are secure starting points and should be adapted per environment and compliance regime.
- Apply firewall and audit rules using change management in staging before production rollout.
