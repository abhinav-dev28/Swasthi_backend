Swasthi Backend API

A production-ready backend service for the Swasthi fitness and wellness platform. Built using FastAPI, SQLModel, and PostgreSQL, with Poetry for dependency and environment management.

🚀 Tech Stack

Python 3.11+

FastAPI – Modern async web framework

SQLModel – ORM for relational models

PostgreSQL – Relational DB (Cloud-hosted)

Alembic – Database migrations

Poetry – Dependency + virtual environment manager

Uvicorn – ASGI server

📁 Project Structure

swasthi_admin_BE/
├── alembic/ # DB migration scripts
├── alembic.ini # Alembic config file
├── scripts/ # Custom startup scripts (e.g., dev.py)
├── src/ # Application source code
│ ├── config/ # Settings, DB connection
│ ├── models/ # SQLModel schemas
│ ├── controllers/ # Business logic
│ ├── routes/ # FastAPI route handlers
│ └── app.py # Main FastAPI app entry
├── venv/ # Poetry-managed virtual environment (auto-created)
├── .env # Environment variables (e.g., DB URL)
├── pyproject.toml # Project configuration (like package.json)
└── README.md # Documentation

🛠️ Step-by-Step Setup Guide

✅ Prerequisites

Install Python 3.11+: Download Python

Ensure you check "Add to PATH" during installation.

Verify installation:

python --version

Install Poetry:

curl -sSL https://install.python-poetry.org | python3 -

# Restart terminal or run:

export PATH="$HOME/.local/bin:$PATH"

Verify poetry is installed:

poetry --version

🚧 Project Setup

# Clone the project

git clone git@github.com:abhinav-dev28/Swasthi_backend.git
cd Swasthi_backend

# Install all dependencies and setup virtual environment

poetry install

# Activate the virtual environment

poetry shell

# Create a .env file in the root and add your database URL

DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<dbname>

▶️ Start Development Server
docker-compose up
docker-compose up --build (if dockerfile or compose-docker file changed)

poetry run dev

To Stop Server
docker-compose down

📦 Add New Dependency

poetry add <package_name>

🔄 Database Migrations with Alembic

1. Configure Alembic

Make sure your alembic/env.py imports all models:

from src.models.employee import Employee # and other models

Also, dynamically set the DB URL:

from src.config.settings import settings
config.set_main_option("sqlalchemy.url", settings.db_url)

2. Create Migration

poetry run alembic revision --autogenerate -m "added employee table"

3. Apply Migration

poetry run alembic upgrade head

ℹ️ If you make changes to existing models, repeat steps 2 and 3.

🧪 Useful Tips

Always run poetry shell when working on this project.

Use .env to manage sensitive configs (never push this file to GitHub).

Use poetry export -f requirements.txt --output requirements.txt if deploying to platforms that don't support poetry.

🤝 Contributing

Follow the setup guide above.

Reach out to the repo maintainer for DB credentials.

Use consistent code formatting (e.g., black, ruff via pre-commit).

📫 Contact

Maintainer – @abhinav-dev28
