# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA gerald_hopkins_workspace.test;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE gerald_hopkins_workspace.test.test_table
# MAGIC AS SELECT 1 AS id, "test data" as value;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(1) FROM gerald_hopkins_workspace.default.songs_raw;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE gerald_hopkins_workspace.default.songs_raw;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT artist_location, COUNT(1) FROM songs_raw GROUP BY artist_location
# MAGIC ORDER BY COUNT(1) DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gerald_hopkins_workspace.default.songs_raw
# MAGIC WHERE artist_location LIKE '%Lakeland%';
