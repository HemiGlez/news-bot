# News-bot

## Goal
NewsBot is a Telegram bot developed in Python that sends up to 3 daily news articles to a Telegram channel based on a user-selected topic.
The bot prevents sending duplicate news and runs automatically every day at 6:30 AM.
The project follows a **hexagonal architecture**, clearly separating the layers:
- `domain` → business logic
- `application` → use cases
- `infrastructure` → persistence and external APIs
- `interfaces` → Telegram interaction

## Installing the environment with Pipenv
The project includes the `Pipfile` and `Pipfile.lock` files to create a virtual environment with all required dependencies.

### Install Pipenv (if you don't have it)

```bash
pip install pipenv
```

### Create and activate the virtual environment
From the project root folder (NewsBot), run:

```bash
pipenv install
pipenv shell
```

### Running the Tests
```bash
pipenv run python -m pytest -v --rootdir=.
```

## Add Settings

To keep your API password and other credentials secure:

1. Copy the `.env.template` file to `.env` in the root folder to create your personal configuration file.  
   ```bash
   cp .env.template .env
   ```
2. Open .env and add your API password and any other required credentials.
3. Ensure .env is listed in .gitignore so it isn’t pushed to Git. Only .env.template should be shared.
