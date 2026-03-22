"""Validate security baseline config files.

Usage:
    python scripts/validate_security_config.py
"""

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
FW_PATH = ROOT / "configs/security/firewall.yaml"
AUDIT_PATH = ROOT / "configs/security/audit.yaml"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must parse into a mapping")
    return data


def validate_firewall(cfg: dict) -> None:
    defaults = cfg.get("default_policy", {})
    for key in ("inbound", "outbound", "east_west"):
        if defaults.get(key) != "deny":
            raise ValueError(f"firewall default_policy.{key} must be 'deny'")

    for section in ("allow_inbound", "allow_outbound", "allow_east_west"):
        rules = cfg.get(section)
        if not isinstance(rules, list) or not rules:
            raise ValueError(f"{section} must be a non-empty list")
        for rule in rules:
            if not rule.get("id"):
                raise ValueError(f"rule in {section} missing id")
            if rule.get("protocol") not in {"tcp", "udp"}:
                raise ValueError(f"rule {rule.get('id')} has invalid protocol")
            ports = rule.get("ports")
            if not isinstance(ports, list) or not ports:
                raise ValueError(f"rule {rule.get('id')} must include ports")


def validate_audit(cfg: dict) -> None:
    scopes = cfg.get("audit_scopes", {})
    required = {"auth", "config", "data", "runtime"}
    missing = required - set(scopes.keys())
    if missing:
        raise ValueError(f"audit_scopes missing: {', '.join(sorted(missing))}")

    retention = cfg.get("retention", {})
    for key in ("hot_days", "warm_days", "cold_days"):
        if not isinstance(retention.get(key), int) or retention[key] <= 0:
            raise ValueError(f"retention.{key} must be a positive integer")

    integrity = cfg.get("integrity", {})
    if not integrity.get("log_signing"):
        raise ValueError("integrity.log_signing must be true")
    if not integrity.get("tamper_alerting"):
        raise ValueError("integrity.tamper_alerting must be true")


def main() -> int:
    fw_cfg = load_yaml(FW_PATH)
    audit_cfg = load_yaml(AUDIT_PATH)
    validate_firewall(fw_cfg)
    validate_audit(audit_cfg)
    print("Security configuration validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
