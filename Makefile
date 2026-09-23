.PHONY: check

check:
	python -m compileall -q brazil_data_map tests
	python -m brazil_data_map validate-registry
	python -m unittest discover -s tests -v
