site_install:
	pip install -r requirements.txt

site_preview: site_build
	python -m http.server 8000 --directory site

site_build:
	python scripts/build_site.py

site_deploy:
	@echo "Static deploy is environment-specific; publish ./site with your host."

security_audit:
	python scripts/validate_security_config.py


codexx_demo:
	python scripts/codexx_demo.py

test:
	python -m unittest discover -s tests


formal_audit:
	python scripts/codex_formal_audit.py
