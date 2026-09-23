$ErrorActionPreference = "Stop"

python -m compileall -q brazil_data_map tests
python -m brazil_data_map validate-registry
python -m brazil_data_map validate-distribution-profile
python -m unittest discover -s tests -v
