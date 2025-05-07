# Airflow Demo

This repository contains a demo Apache Airflow project configured with Docker Compose and Poetry for dependency management.

## Prerequisites

- Docker and Docker Compose
- Python 3.11+
- Git

## Getting Started with Poetry

### Installing Poetry

Poetry is a dependency management and packaging tool for Python. It allows you to declare the libraries your project depends on and manages them for you.

```bash
# Install Poetry
pip install poetry

# Verify installation
poetry --version
```

### Configuring Poetry

It's recommended to configure Poetry to create virtual environments in your project directory for better visibility and management:

```bash
# Configure Poetry to create virtualenvs in project directory
poetry config virtualenvs.in-project true
```

Alternatively, you can set the environment variable:

```bash
# Environment variable approach
export POETRY_VIRTUALENVS_IN_PROJECT=true
```

For Windows users, you can set this in PowerShell:
```powershell
$env:POETRY_VIRTUALENVS_IN_PROJECT=true
```

### Project Setup

Clone the repository and install dependencies:

```bash
# Clone the repository (if you haven't already)
git clone <repository-url>
cd airflow-demo

# Install dependencies
poetry install
```

This will create a `.venv` directory in your project and install all dependencies specified in `pyproject.toml`.

### Activating the Virtual Environment

```bash
# Activate the virtual environment
poetry shell
```

## Running Airflow with Docker Compose

This project uses Docker Compose to set up a complete Airflow environment with PostgreSQL and Redis.

```bash
# Start the Airflow services
docker-compose up -d
```

The Airflow web interface will be available at [http://localhost:9080](http://localhost:9080).

- Username: `airflow`
- Password: `airflow`

## Project Structure

- `dags/`: Contains Airflow DAG definitions
  - `hello_world_dag.py`: A simple "Hello World" DAG
  - `hello_tasks_dag.py`: Demonstrates parallel task execution
- `logs/`: Contains Airflow logs
- `plugins/`: For Airflow plugins

## Available DAGs

### 1. hello_world

A simple DAG that prints "Hello, Airflow!" to the logs.

### 2. hello_tasks_dag

Demonstrates three tasks running in parallel, each sleeping for 10 seconds before completion.

## Stopping the Services

```bash
# Stop the Airflow services
docker-compose down

# To also remove volumes (database data)
docker-compose down -v
```

## Development

To add new dependencies to your project:

```bash
# Add a new dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name
```

## Troubleshooting

- **Permission Issues**: If you encounter permission issues with the logs directory, check the `AIRFLOW_UID` in your `.env` file and ensure it matches your user ID.
- **Database Connection Issues**: Ensure PostgreSQL is running and the connection details in `docker-compose.yaml` are correct.
- **Redis Connection Issues**: Check that Redis is running on port 6380 (host) / 6379 (container).

## Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- 
