# Security Baseline: Firewall, Headers, and Audit

This directory contains a deployable baseline for perimeter defense and security observability.

## Files
- `firewall/iptables.rules.v4`: default-deny IPv4 firewall with only SSH/HTTP/HTTPS ingress.
- `nginx/security_headers.conf`: secure response headers and CSP for static/docs deployments.
- `audit/auditd.rules`: host-level audit watches for identity, privilege, SSH, NGINX, and webroot changes.

## Apply

### Firewall
```bash
sudo iptables-restore < security/firewall/iptables.rules.v4
```

### NGINX headers
Include in a server block:
```nginx
include /path/to/security/nginx/security_headers.conf;
```

### auditd
```bash
sudo cp security/audit/auditd.rules /etc/audit/rules.d/99-awesome-python.rules
sudo augenrules --load
```
