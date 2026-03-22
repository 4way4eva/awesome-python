"""Build a lightweight static site from repository markdown files."""

from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DOCS = ROOT / "docs"

PAGES = [
    ("Home", ROOT / "README.md", SITE / "index.html"),
    (
        "Security Baseline",
        DOCS / "security-firewall-audit.md",
        SITE / "security-firewall-audit" / "index.html",
    ),
    (
        "Creative Pack",
        DOCS / "blue-signal-creative-pack.md",
        SITE / "blue-signal-creative-pack" / "index.html",
    ),
    (
        "CODEXX Demo",
        DOCS / "codexx-demo.md",
        SITE / "codexx-demo" / "index.html",
    ),
    (
        "Ceremonial Report",
        DOCS / "ceremonial-codex-report.md",
        SITE / "ceremonial-codex-report" / "index.html",
    ),
    (
        "EV0LClock Research",
        DOCS / "evolclock-deep-research.md",
        SITE / "evolclock-deep-research" / "index.html",
    ),
    (
        "Formal Edition Audit",
        DOCS / "formal-edition-audit.md",
        SITE / "formal-edition-audit" / "index.html",
    ),
    (
        "Codex Scroll AR",
        DOCS / "codex-scroll-ds-baba-ar.md",
        SITE / "codex-scroll-ds-baba-ar" / "index.html",
    ),
    (
        "BLEU Day of Thanks",
        DOCS / "bleu-day-of-thanks.md",
        SITE / "bleu-day-of-thanks" / "index.html",
    ),
    (
        "EV0L Decoded Insights",
        DOCS / "evol-codex-decoded-insights.md",
        SITE / "evol-codex-decoded-insights" / "index.html",
    ),
]


def render(markdown_text: str, title: str) -> str:
    body = markdown.markdown(markdown_text, extensions=["fenced_code", "tables", "toc"])
    nav = "".join(
        [
            '<a href="/">Home</a>',
            '<a href="/security-firewall-audit/">Security Baseline</a>',
            '<a href="/blue-signal-creative-pack/">Creative Pack</a>',
            '<a href="/codexx-demo/">CODEXX Demo</a>',
            '<a href="/ceremonial-codex-report/">Ceremonial Report</a>',
            '<a href="/evolclock-deep-research/">EV0LClock Research</a>',
            '<a href="/formal-edition-audit/">Formal Edition Audit</a>',
            '<a href="/codex-scroll-ds-baba-ar/">Codex Scroll AR</a>',
            '<a href="/bleu-day-of-thanks/">BLEU Day of Thanks</a>',
            '<a href="/evol-codex-decoded-insights/">EV0L Decoded Insights</a>',
        ]
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>{title}</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 920px; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
nav {{ display: flex; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap; }}
code {{ background: #f4f4f4; padding: 0.1rem 0.3rem; }}
pre {{ background: #111; color: #f7f7f7; padding: 1rem; overflow-x: auto; }}
</style>
</head>
<body>
<nav>{nav}</nav>
<main>{body}</main>
</body>
</html>"""


def main() -> None:
    if SITE.exists():
        for p in sorted(SITE.rglob("*"), reverse=True):
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                try:
                    p.rmdir()
                except OSError:
                    pass
    SITE.mkdir(parents=True, exist_ok=True)

    for title, src, dest in PAGES:
        content = src.read_text(encoding="utf-8")
        html = render(content, title)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")

    print(f"Site built at {SITE}")


if __name__ == "__main__":
    main()
