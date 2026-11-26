# TestingClaudeManagedAgents

This is a sample repository for the dev-fixer agent POC. To run the tests, install the dependencies with `pip install -r requirements-dev.txt`, then run `pytest -q`.

## Internal dependencies

`requirements-internal.txt` lists packages published only on Cybage's internal registry.
Don't install them from pypi.org. Get the index URL and the approved versions from the
internal package API (`get_internal_package` tool), then install with `pip install --user`.
