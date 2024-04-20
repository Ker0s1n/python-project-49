install: # installing poetry on the first clone or after changing dependencies
	poetry install


brain-games: # launching the module brain_games.py from the brain_games/scripts directory/
	poetry run brain-games


build: # starting the package build and confirming the correct configuration
	poetry build


publish: # start debugging the publish argument is used to avoid adding the package to the PyPI directory
	poetry publish --dry-run


package-install: # installing the package from the operating system - run from the root directory of the project
	python3 -m pip install --user dist/*.whl
