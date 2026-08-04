# Databricks DAB Template

This repository is a simple starter template for Databricks Asset Bundles (DAB). In short, it shows how to structure a Databricks project with:

- a bundle definition in databricks.yml
- a sample job definition in resources/sample_job.yml
- example Python tasks under src/ that can be run as part of a job
- a basic Python project setup for local development and testing

This is a template repository. Clone it, rename it to fit your project, and customize the sample job and code for your own use case.

## Repository structure

- databricks.yml: main bundle configuration and target settings
- resources/sample_job.yml: sample Databricks job definition
- src/task_1.py and src/task_2.py: example notebook tasks
- pyproject.toml: Python project metadata and development dependencies
- tests/: placeholder test location

## Before you use it

Before deploying or running this template, make sure the following configuration is updated:

1. Update the config
   - update the environment variables and databricks host(url) in the databricks.yml file
   - update the default catalog and schema values

2. Authenticate to Databricks
   - This repo, currently authenticates through databricks host and token configured
   - Update the DATABRICKS_HOST (format: https://adb-1234567890123456.00.azuredatabricks.net)
   - Update the DATABRICKS_TOKEN (personal token)
   - It is strongly recommended to use service priniciple in real-time projects

3. Jobs and notebooks update
   - update the jobs and notebooks as per requirements

4. Databricks bundle validate
   - Authenticate from local and do databricks bundle valid