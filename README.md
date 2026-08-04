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
- src/task_1.py and src/task_2.py: example Python tasks
- pyproject.toml: Python project metadata and development dependencies
- tests/: placeholder test location

## Before you use it

Before deploying or running this template, make sure the following configuration is updated:

1. Rename and config
   - Update the project name in pyproject.toml.
   - update the environments and 

2. Configure your Databricks workspace
   - Update the workspace host in databricks.yml for your environment.
   - Set the catalog and schema values under the dev target.

3. Provide a valid cluster
   - Replace the example cluster ID in resources/sample_job.yml with an existing Databricks cluster ID in your workspace.

4. Authenticate to Databricks
   - Install the Databricks CLI.
   - Authenticate using your Databricks workspace credentials, for example with:
     - databricks auth login

5. Install local dependencies
   - Create and activate a Python environment.
   - Install the project and dev dependencies, for example:
     - pip install -e .
     - pip install pytest ruff databricks-dlt "databricks-connect>=15.4,<15.5" ipykernel

## Quick start

After the configuration above is complete, you can validate and deploy the bundle:

- databricks bundle validate
- databricks bundle deploy

You can then customize the sample job, replace the example tasks, and add your own logic.

