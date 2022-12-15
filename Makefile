reformat:
	black --target-version py310 app
	isort app

lint:
	flake8 app

test:
	pytest
