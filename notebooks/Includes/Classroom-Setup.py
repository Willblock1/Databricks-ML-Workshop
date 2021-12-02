# Databricks notebook source
username = spark.sql("SELECT current_user()").collect()[0][0]

spark.conf.set("com.databricks.training.username", username)

displayHTML("Initialized classroom variables & functions...")

# COMMAND ----------

course_name = "idbml"

username = spark.conf.get("com.databricks.training.username", "unknown-username")

dbutils.fs.mkdirs("dbfs:/user/" + username)
dbutils.fs.rm("dbfs:/user/" + username + "/" + course_name, True)
dbutils.fs.mkdirs("dbfs:/user/" + username + "/" + course_name)

database_name = username + "_" + course_name
database_name = database_name.replace(".", "_").replace("@", "_")


try:
    spark.sql(f"CREATE DATABASE {database_name}")
except:
    None

base_read_path = "wasbs://courseware@dbacademy.blob.core.windows.net/introduction-to-databricks-machine-learning/v01/"
london_read_path = base_read_path + "london/"
base_write_path = "dbfs:/user/" + username + "/" + course_name + "/"


input_path = london_read_path + "london-listings-2021-01-31"


None

