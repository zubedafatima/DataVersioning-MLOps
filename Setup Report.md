
# Data Preprocessing and DVC Setup Report

## Introduction

This document outlines the workflow and methodology of the data preprocessing and DVC setup for our Apache Airflow orchestrated pipeline. The goal of the project is to automate the extraction, transformation, and loading (ETL) of article data from news websites, using Data Version Control (DVC) for managing data storage and versioning.

## Workflow Description

The workflow consists of a Directed Acyclic Graph (DAG) defined in Apache Airflow that includes three main tasks: extraction, transformation, and loading. Each task is designed to handle specific aspects of the ETL process.

### 1. Extraction Task

**Function**: `extract`

- **Purpose**: To fetch articles from specified URLs and extract relevant details such as title and URL.
- **Methodology**: The function uses the `requests` library to make HTTP requests to the target websites (Dawn.com and BBC.com). It then parses the HTML content using `BeautifulSoup` to extract links (anchor tags).
- **Data Collected**: Each article's source, title, and URL are collected and stored in a Pandas DataFrame, which is then written to a CSV file (`/tmp/extracted_articles.csv`).

### 2. Transformation Task

**Function**: `transform`

- **Purpose**: To clean and prepare the extracted data for loading.
- **Methodology**: This function reads the data from the CSV file created by the extract function. It uses Pandas to remove duplicate entries based on URLs and drop any rows where the title is missing. The cleaned data is saved back to a new CSV file (`/tmp/transformed_articles.csv`).

### 3. Loading Task

**Function**: `load`

- **Purpose**: To manage and version control the processed data using DVC.
- **Methodology**: The function adds the transformed CSV file to DVC tracking using the command `dvc add`. It then pushes this data to a configured DVC remote storage using `dvc push -r myremote`, ensuring that the data versioning is maintained.

## DVC Integration

- **Configuration**: DVC is integrated to handle large data files and their versioning outside of Git, allowing efficient data management within the constraints of a version-controlled environment.
- **Remote Storage**: Data is stored remotely, typically in cloud storage, to ensure data persistence and scalability.

## Airflow Configuration

- **DAG Setup**: Defined with specific start dates, retry policies, and execution intervals to ensure that the ETL process runs smoothly and reliably.
- **Task Dependencies**: Proper sequencing is established where the extract task feeds into the transform task, which in turn feeds into the load task.

## Challenges and Considerations

- **Error Handling**: Proper error handling mechanisms are essential to manage the potential failures in data extraction or processing.
- **Data Quality**: Ensuring the cleanliness and reliability of the data through rigorous transformation rules is crucial for maintaining the integrity of the dataset.

## Conclusion

This setup provides a robust framework for automating data pipelines with advanced data management and version control using Apache Airflow and DVC. The project demonstrates a practical implementation of MLOps practices suitable for scalable and reproducible data workflows.
