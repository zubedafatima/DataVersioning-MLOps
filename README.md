
# Apache Airflow with Docker, DVC, and Git Integration

This project demonstrates a robust data processing pipeline using Apache Airflow, orchestrated within Docker containers. The data versioning is managed through Data Version Control (DVC) with Git for source control, showcasing a modern MLOps workflow.

## Project Overview

The project sets up Apache Airflow in Docker containers using Docker Compose for an easy and reproducible environment setup. It integrates DVC for data management and versioning, and uses Git for code versioning, providing a comprehensive environment for data pipeline management.

## Installation

### Prerequisites

- Docker and Docker Compose
- Git
- Python 3.8+ (for running scripts locally if necessary)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Initialize DVC**:
    ```bash
    dvc init
    ```

3. **Run Docker Compose** to set up the Airflow environment:
    ```bash
    docker-compose up -d
    ```

4. **Access Airflow**:
    Navigate to `http://localhost:8080` to access the Airflow web interface.

## Usage

1. **Start the Airflow services** using Docker Compose:
    ```bash
    docker-compose up -d
    ```

2. **Navigate to the Airflow UI** at `http://localhost:8080` and trigger the DAGs manually.

3. **Main.py**: This Python script defines the DAGs which automate the data extraction, transformation, and loading processes. It integrates Git and DVC to manage and version the data and code.
