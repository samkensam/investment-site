## Copilot instructions for investment_site

Purpose: short, actionable guidance so an AI coding agent can be productive immediately.

### Big picture
- Single Django project package: [investment_site](../investment_site). No apps scaffolded yet; routing currently only registers the admin in [investment_site/urls.py](../investment_site/urls.py).
- Settings live in [investment_site/settings.py](../investment_site/settings.py). The project uses SQLite (`db.sqlite3`) and `DEBUG = True` by default.

### Run & dev workflow (Windows)
- Activate virtualenv (PowerShell):

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- Install framework (if missing): `pip install Django==4.2.27` — add new deps to `requirements.txt` when introduced.
- Common commands (run from repo root):

  ```bash
  python manage.py migrate
  python manage.py makemigrations <app>
  python manage.py runserver
  ```

### Key files to inspect
- [manage.py](../manage.py) — Django CLI
- [investment_site/settings.py](../investment_site/settings.py) — DB, DEBUG, INSTALLED_APPS, TEMPLATES
- [investment_site/urls.py](../investment_site/urls.py) — current URL surface
- [investment_site/wsgi.py](../investment_site/wsgi.py) and [investment_site/asgi.py](../investment_site/asgi.py) — deployment entrypoints

### Project-specific conventions (discoverable
- `TEMPLATES['DIRS'] = []` and `APP_DIRS = True` — place templates under app-level `templates/` directories (e.g., `myapp/templates/myapp/*.html`).
- New Django apps must be added to `INSTALLED_APPS` in [investment_site/settings.py](../investment_site/settings.py).
- The repository currently stores `SECRET_KEY` in plaintext. Do not commit changes that expose secrets; prefer env-based overrides if you change this.

### When modifying the project
- Adding models: run `python manage.py makemigrations <app>` then `python manage.py migrate`; commit the generated migrations.
- Adding dependencies: create/update `requirements.txt` and pin versions (e.g., `Django==4.2.27`).
- Adding templates: either add them under `templates/` inside an app, or update `TEMPLATES['DIRS']` in settings.

### Debugging & deployment notes
- `DEBUG = True` produces detailed errors locally. For deployment, set `DEBUG = False` and configure `ALLOWED_HOSTS` in [../investment_site/settings.py](../investment_site/settings.py).
- Confirm `WSGI_APPLICATION` / `ASGI_APPLICATION` entries when deploying; they point to `investment_site.wsgi.application` / `investment_site.asgi.application`.

### Integrations & infra
- No external services (Redis, Celery, external DBs) are configured; add and document any integration in `settings.py` and this file.

### Examples & search targets
- See [investment_site/settings.py](../investment_site/settings.py) for DB and debug settings.
- See [investment_site/urls.py](../investment_site/urls.py) for current routing (admin-only).

If you want this shortened further or to include CI/test commands, tell me which areas to expand.
lm# Copilot instructions for investment_site

This project is a minimal Django site scaffolded with Django 4.2.27. These notes help AI coding agents be immediately productive and avoid incorrect assumptions.

- **Big picture**: single Django project named `investment_site` (project package at `investment_site/`). No apps are present yet; URL routing is minimal (`investment_site/urls.py` only registers the admin). Settings and app wiring live in `investment_site/settings.py`.

- **Run & dev workflow (Windows)**:
  - Activate venv: `./venv/Scripts/Activate.ps1` (PowerShell) or `./venv/Scripts/activate` (cmd).
  - Install dependencies if missing: `pip install Django==4.2.27` (no `requirements.txt` in repo).
  - Run server: `python manage.py runserver` from repo root.
  - Database: SQLite at `BASE_DIR / db.sqlite3` (configured in `investment_site/settings.py`). Use `python manage.py migrate` and `python manage.py makemigrations` for schema changes.

- **Key files**:
  - `manage.py` — CLI entry for Django commands.
  - `investment_site/settings.py` — main configuration (DEBUG=True, SECRET_KEY present, SQLite DB, `INSTALLED_APPS` contains only Django built-ins).
  - `investment_site/urls.py` — URL routing (currently only `admin/`).
  - `investment_site/wsgi.py` and `investment_site/asgi.py` — deployment interfaces.

- **Project-specific patterns & conventions (discoverable)**:
  - Settings keep `TEMPLATES['DIRS'] = []` and `APP_DIRS = True` — put templates under app-level `templates/` directories by default.
  - New apps should be added to `INSTALLED_APPS` in `investment_site/settings.py`.
  - The repo currently stores the SECRET_KEY in plaintext in `settings.py`; avoid changing it without adding an env-based override if committing to a shared repo.

- **What AI agents should do when changing code**:
  - If you add models, run `python manage.py makemigrations <app>` and `python manage.py migrate` — ensure migrations are created and checked into git.
  - If you add templates, either place them in an app `templates/` directory or update `TEMPLATES['DIRS']`.
  - When adding third-party packages, update a `requirements.txt` (create one) with pinned versions (e.g., `Django==4.2.27`).

- **Debugging hints**:
  - With `DEBUG = True` (current settings), detailed error pages are shown locally; check `ALLOWED_HOSTS` when debugging remote access.
  - For runtime issues in deployment, confirm `WSGI_APPLICATION` / `ASGI_APPLICATION` point to `investment_site.wsgi.application` / `investment_site.asgi.application`.

- **Integration & infra notes (discoverable)**:
  - No external services, caches, or message brokers are configured in the repo; integrations must be added explicitly in `settings.py` and documented in code changes.

- **Searchable examples**:
  - Look at `investment_site/settings.py` to confirm DB, DEBUG, and installed apps.
  - Look at `investment_site/urls.py` to understand current routing surface.

If anything here is unclear or you want more project-specific examples (tests, app patterns, CI commands), tell me what to extract next and I'll iterate.
