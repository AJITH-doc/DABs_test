# Databricks DAB Template

This repository is a simple starter template for Databricks Asset Bundles (DAB). In short, it shows how to structure a Databricks project with:

- a bundle definition in databricks.yml
- a sample job definition in resources/sample_job.yml
- example Python tasks under src/ that can be run as part of a job
- a basic Python project setup for local development and testing

This is a template repository. Clone it, rename it to fit your project, and customize the sample job and code for your own use case.

## Repository structure

The project is organized into a few simple folders so configuration, code, and deployment assets stay separated.

```text
databricks_dab_template/
├── .github/
│   └── workflows/
├── resources/
│   └── sample_job.yml
├── src/
│   ├── task_1.py
│   └── task_2.py
├── tests/
│   └── sample_test.py
├── databricks.yml
├── README.md
└── .gitignore
```

### What each part is for

- .github/workflows/: contains CI/CD workflow files for automation such as deployment pipelines
- resources/: holds Databricks resource definitions, including the sample job configuration
- src/: contains the Python source files that define your job tasks or logic
- tests/: stores test files for validating your code locally
- databricks.yml: the main Databricks Asset Bundle configuration file
- README.md: project documentation and usage instructions
- .gitignore: lists files and folders that should not be committed to Git

## Before you use it

Before deploying or running this template, make sure the following configuration is updated:

1. Update the config
   - update the environment variables and databricks host(url) in the databricks.yml file
   - update the default catalog and schema values

2. Authenticate to Databricks
   - This repo, currently authenticates through databricks host and token configured
   - Update the below secrets in github which will be used in github workflow deployments
   - DATABRICKS_HOST (format: https://adb-1234567890123456.00.azuredatabricks.net)
   - DATABRICKS_TOKEN (personal token)
   - It is strongly recommended to use service priniciple in real-time projects

3. Jobs and notebooks update
   - update the jobs and notebooks as per requirements

4. Databricks bundle validate
   - Authenticate from local and do databricks bundle valid