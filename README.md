# Czysty kod 2022/2023

# Workflow
- Each change should be done via a PR from a new branch
- Approvals are not needed if the change is small
- Make sure the `CI` checks and tests are passing before merging

# Codestyle
- Use type hints everywhere you can
- Adhere to PEP8
- Use `black` for auto formatting
- Use `isort` to automatically sort imports
- Use `flake8` for linting

You can use the provided `Makefile` to adhere to these standards.

# Development
Development is done via `docker-compose.yml` file. Make sure you have `docker` installed and run:
```
docker-compose up --build
```
