.DEFAULT_GOAL := help

.PHONY: help
help: 
	@echo "\n * push-to-pypi"
	@echo "\n"

.PHONY: push-to-pypi
push-to-pypi: 
	-rm -r dist/* 
	bumpversion --allow-dirty patch pyproject.toml
	python3 -m build
	python3 -m twine upload --skip-existing --repository pypi dist/* --username "jls-praxis" --password "m?iY#K8\$$Qdt4XjAT"

.PHONY: update-component
update-component: 
	@echo "\n || Remember to export KFPLIBCOMPONENT=xxx ||"
	make push-to-pypi
	sleep 10
	(cd ../dream-kfp-components && make build-component)