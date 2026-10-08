# Databricks DAB Template

This repository is a simple starter template for Databricks Asset Bundles (DAB). In short, it shows how to structure a Databricks project with:

- a bundle definition in databricks.yml
- a Delta Live Tables pipeline definition in resources/sales_pipeline.yml
- a job definition in resources/sample_job.yml that runs the pipeline followed by an aggregation task
- example Python/notebook tasks under src/ that can be run as part of a job or pipeline
- a GitHub Actions workflow that validates and deploys the bundle

This is a template repository. Clone it, rename it to fit your project, and customize the sample job and code for your own use case.

## Repository structure

The project is organized into a few simple folders so configuration, code, and deployment assets stay separated.

```text
databricks_dab_template/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── resources/
│   ├── sales_pipeline.yml
│   └── sample_job.yml
├── src/
│   ├── sales_pipeline.py
│   └── agg_task.py
├── databricks.yml
├── README.md
└── .gitignore
```

### What each part is for

- .github/workflows/deploy.yml: CI/CD workflow that validates and deploys the bundle on pull requests to dev/main or via manual dispatch
- resources/sales_pipeline.yml: defines the `sales_pipeline` Delta Live Tables pipeline (serverless), backed by src/sales_pipeline.py
- resources/sample_job.yml: defines `sample_job`, which runs the DLT pipeline (`dlt_pipeline` task) followed by the aggregation task (`agg_task`), on an hourly (paused) schedule
- src/sales_pipeline.py: DLT notebook that builds the silver-layer sales tables (filters payments, enriches with customer data)
- src/agg_task.py: notebook that aggregates the enriched silver table into a gold summary table
- databricks.yml: the main Databricks Asset Bundle configuration file, including the `catalog`/`schema` variables and the `dev` target (a commented-out `prod` target is included as an example)
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
   - `agg_task` in resources/sample_job.yml currently runs on a hardcoded `existing_cluster_id` — replace this with your own cluster id or switch to a job cluster/serverless
   - src/sales_pipeline.py and src/agg_task.py currently reference the `ingestion_cat.test` catalog/schema directly — update these to match your environment (or parameterize them using the `catalog`/`schema` bundle variables)
   - the job schedule in resources/sample_job.yml is set to hourly and `pause_status: PAUSED` — update as needed before relying on it

4. Databricks bundle validate
   - Authenticate from local and do databricks bundle valid.