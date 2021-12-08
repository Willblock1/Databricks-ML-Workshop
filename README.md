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
* [ML Flow Guide](https://docs.databricks.com/applications/mlflow/index.html)
* [Databricks ML Blogs](https://databricks.com/blog/category/engineering/data-science-machine-learning)
* [Databricks Feature Store Blog](https://databricks.com/blog/2021/05/27/databricks-announces-the-first-feature-store-integrated-with-delta-lake-and-mlflow.html)
* [Databricks AutoML Blog](https://databricks.com/blog/2021/05/27/introducing-databricks-automl-a-glass-box-approach-to-automating-machine-learning-development.html)
* [Solution Accelerators](https://databricks.com/solutions/accelerators)

# Workshop Flow

The workshop consists of 6 interactive sections that are separated by notebooks located in the notebooks folder in this repository.
|Notebook|Summary|
|--------|-------|
|`IDBML 02 - Creating a Feature Table.py`|Feature engineering and creating feature table in the Databricks Feature Store|
|`IDBML 03 - Creating a Model with AutoML.py`|Create Model experimentation with Databricks AutoML|
|`IDBML 04a - Registering a Model.py`|Registering a Model in a model registry|
|`IDBML 04b - Implementing a Webhook.py`|Implementing a web hook as a model is transitioned|
|`IDBML 05 - Deploying a Model for Batch Inference.py`|Deploy model for batch inference|
|`IDBML 06 - Scheduling a Machine Learning Workflow.py`|Scheduling the ML workflow using Databricks jobs|

We will be going through these notebooks live during today's session. See the power of Databricks ML and understand how you can use ML Flow, Databricks Feature Store and Databricks AutoML to drastically simplify your end-to-end model lifecycle.


# Setup / Requirements

This workshop requires a running Databricks workspace. If you are an existing Databricks customer, you can use your existing Databricks workspace. Otherwise, the notebooks in this workshop have been tested to run on [Databricks Community Edition](https://databricks.com/product/faq/community-edition) as well.

## DBR Version

The features used in this workshop require `DBR 8.4 ML and above`.

## Repos

If you have repos enabled on your Databricks workspace. You can directly import this repo and run the notebooks as is and avoid the DBC archive step.

## DBC Archive

Download the DBC archive from the dbc-archive folder and import the archive into your Databricks workspace.
