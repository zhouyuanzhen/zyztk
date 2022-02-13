all: clean check_setup build_bdist pypi_upload
	@echo "All in one workflow"

check_setup:
	@python3 setup.py check

build_sdist: check_setup
	@echo "build sdist:"
	@python3 setup.py sdist

build_bdist: check_setup
	@echo "build bdist_wheel:"
	@python3 setup.py bdist_wheel

pypi_upload: build_bdist
	@echo "Upload to PyPI:"
	@twine upload dist/*

clean:
	@echo "Clean workspace:"
	rm -fr build dist zhouyuanzhen.egg-info
