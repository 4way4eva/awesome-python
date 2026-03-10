from pathlib import Path
import sys

REQUIRED = {
    Path("security/firewall/iptables.rules.v4"): [
        ":INPUT DROP",
        "--dport 22",
        "--dport 80",
        "--dport 443",
    ],
    Path("security/nginx/security_headers.conf"): [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
    ],
    Path("security/audit/auditd.rules"): [
        "-w /etc/ssh/sshd_config",
        "-k rootcmd",
    ],
}


def main() -> int:
    missing = []
    for path, markers in REQUIRED.items():
        if not path.exists():
            missing.append(f"missing file: {path}")
            continue
        content = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                missing.append(f"{path}: missing marker '{marker}'")

    if missing:
        print("Security baseline validation failed:")
        for item in missing:
            print(f" - {item}")
        return 1

    print("Security baseline validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
