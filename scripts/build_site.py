from pathlib import Path
import shutil
import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

PAGES = [
    (ROOT / "README.md", SITE / "index.html", "Awesome Python"),
    (DOCS / "security-deployment.md", SITE / "security-deployment" / "index.html", "Security Deployment Baseline"),
]


def wrap_html(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title}</title>
  <link rel=\"stylesheet\" href=\"/css/extra.css\" />
  <style>body{{max-width:960px;margin:2rem auto;padding:0 1rem;font-family:Arial,Helvetica,sans-serif;line-height:1.55}} nav a{{margin-right:1rem}}</style>
</head>
<body>
<nav>
  <a href=\"/index.html\">Home</a>
  <a href=\"/security-deployment/\">Security Deployment Baseline</a>
</nav>
<hr />
{body}
</body>
</html>
"""


def main() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True, exist_ok=True)

    css_src = DOCS / "css" / "extra.css"
    css_dst = SITE / "css"
    css_dst.mkdir(parents=True, exist_ok=True)
    if css_src.exists():
        shutil.copy2(css_src, css_dst / "extra.css")

    for src, dst, title in PAGES:
        dst.parent.mkdir(parents=True, exist_ok=True)
        markdown_text = src.read_text(encoding="utf-8")
        html_body = markdown.markdown(markdown_text, extensions=["fenced_code", "tables"])
        dst.write_text(wrap_html(title, html_body), encoding="utf-8")

    print(f"Site built at {SITE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
