# Introduction : Databricks ML Workshop

Welcome to the repository for the ML Workshop!

This repository contains the notebooks that are used in the workshop to demonstrate the use of ML.

- [Introduction : Databricks ML Workshop](#introduction-databricks-ml-workshop)
- [Reading Resources](#reading-resources)
- [Workshop Flow](#workshop-flow)
  - [Generator](#generator)
- [Setup / Requirements](#setup--requirements)
  - [DBR Version](#dbr-version)
  - [Repos](#repos)
  - [DBC Archive](#dbc-archive)

# Reading Resources

* [Lakehouse Whitepaper](https://databricks.com/wp-content/uploads/2020/12/cidr_lakehouse.pdf)
* [Delta Lake Primer](https://databricks.com/wp-content/uploads/2019/01/Databricks-Delta-Technical-Guide.pdf)
* [ML Flow Guide] (https://docs.databricks.com/applications/mlflow/index.html)
* [ML Flow Autologging](https://docs.databricks.com/applications/mlflow/databricks-autologging.html)

# Workshop Flow

The workshop consists of 4 interactive sections that are separated by notebooks located in the notebooks folder in this repository.
|Notebook|Summary|
|--------|-------|
|`IDBML 02 - Creating a Feature Table.py`|Feature engineering and creating feature table in the feature store|
|`IDBML 03 - Creating a Model with AutoML.py`|Create Model experimentation with autoML|
|`IDBML 04a - Registering a Model.py`|Registering a Model in a model registry|
|`IDBML 04b - Implementing a Webhook.py`|Implementing a web hook as a model is transitioned|
|`IDBML 05 - Deploying a Model for Batch Inference.py`|Deploy model for batch inference|
|`IDBML 06 - Scheduling a Machine Learning Workflow.py`|Scheduling the ML workflow using Databricks jobs|


# Setup / Requirements

This workshop requires a running Databricks workspace. If you are an existing Databricks customer, you can use your existing Databricks workspace. Otherwise, the notebooks in this workshop have been tested to run on [Databricks Community Edition](https://databricks.com/product/faq/community-edition) as well.

## DBR Version

The features used in this workshop require `DBR 8.4 and above`.

## Repos

If you have repos enabled on your Databricks workspace. You can directly import this repo and run the notebooks as is and avoid the DBC archive step.

## DBC Archive

Download the DBC archive from releases and import the archive into your Databricks workspace.
