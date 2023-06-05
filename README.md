
# Sparkify Music Streaming ETL Pipeline

This project focuses on building an ETL (Extract, Transform, Load) pipeline for Sparkify, a music streaming startup. The goal is to migrate their processes and data to the cloud using AWS services and a data warehouse hosted on Redshift. The pipeline extracts data from JSON logs stored in Amazon S3, stages it in Redshift, and transforms it into dimensional and fact tables. These tables will enable the analytics team to gain insights into the songs that users are listening to.

## Project Description

The project involves the following key steps:

1.  Creation of staging tables in Redshift to store the data retrieved from S3.
2.  Transformation of the staged data into a star schema consisting of fact and dimension tables.
3.  Loading the transformed data into the corresponding fact and dimension tables in Redshift.
4.  Enabling the analytics team to query the data in the dimensional model for song play analysis.

## Project Datasets

The project utilizes two datasets:

-   **Song Data**: A subset of the Million Song Dataset containing JSON files with metadata about songs and artists. The data is partitioned based on the first three letters of the song's track ID.
-   **Log Data**: JSON log files containing user activity on the music streaming app. The log files are partitioned by year and month.

## Schema for Song Play Analysis

The schema chosen for this project is a star schema, which consists of a central fact table and multiple dimension tables.

### Fact Table

-   **songplays**: Records in the event data associated with song plays. This table includes details such as the song play ID, start time, user ID, song ID, artist ID, session ID, location, and user agent.

### Dimension Tables

-   **users**: Information about users in the app, including user ID, first name, last name, gender, and subscription level.
-   **songs**: Details about songs in the music database, including song ID, title, artist ID, year of release, and duration.
-   **artists**: Information about artists in the music database, including artist ID, name, location, latitude, and longitude.
-   **time**: Timestamps of records in the songplays table, broken down into specific units such as hour, day, week, month, year, and weekday.

## Project Files

The project includes the following files:

1.  **create_table.py**: Python script to connect to the Redshift cluster and create the necessary fact and dimension tables.
2.  **etl.py**: Python script to load data from S3 into staging tables on Redshift, and then transform and load the data into the analytics tables.
3.  **testings.ipynb**: This notebook/script sets up an AWS Redshift cluster, retrieves data from an S3 bucket, performs IAM role and security group configurations, displays cluster properties, and conducts data analysis tasks.
4.  **sql_queries.py**: Contains the SQL statements used by the other scripts to create tables, insert data, and perform transformations.
5.  **dwh.cfg**: Configuration file containing important parameters, including AWS access credentials, Redshift cluster details, and file paths.
6.  **README.md**: This file, providing an overview of the project, its components, and instructions for execution.

## Getting Started

To execute the ETL pipeline and analyze the song play data, follow these steps:

1.  Set up the AWS Redshift cluster and IAM role with appropriate permissions.
2.  Update the `dwh.cfg` file with the necessary configuration details.
3.  Run the `create_table.py` script to create the staging, fact, and dimension tables.
4.  Execute the `etl.py` script to load and transform the data from S3 into the Redshift tables.
5.  Perform analytics by running queries on the created tables in the Redshift database.

## Conclusion

The Sparkify Music Streaming ETL Pipeline enables the
migration of data to the cloud and provides a scalable solution for analyzing song play data. By leveraging AWS services and Redshift, the analytics team can gain valuable insights into user behavior and song preferences.

Also in **testings.ipynb** one can find scripts that analyze data by calculating various statistics and generating reports. It uses the `tabulate` library to create a formatted table displaying categories and their corresponding counts. Additionally, it executes SQL queries on a Redshift cluster to find the most active users based on the number of songs played and the most popular songs based on the number of times they have been played. The results are displayed as query outputs showing the relevant data.