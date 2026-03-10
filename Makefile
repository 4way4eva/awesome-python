site_install:
	pip install -r requirements.txt

site_link:
	ln -sf $(CURDIR)/README.md $(CURDIR)/docs/index.md

site_preview: site_build
	python scripts/serve_site.py

site_build:
	python scripts/build_site.py

site_deploy: site_build
	@echo "Deploy step is environment-specific; upload ./site to your host or object storage."

security_audit:
	python scripts/validate_security_baseline.py
