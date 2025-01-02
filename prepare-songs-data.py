# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gerald_hopkins_workspace.default.prepared_songs
# MAGIC   (
# MAGIC     artist_id STRING,
# MAGIC     artist_name STRING,
# MAGIC     duration DOUBLE,
# MAGIC     release STRING,
# MAGIC     tempo DOUBLE,
# MAGIC     time_signature DOUBLE,
# MAGIC     title STRING,
# MAGIC     year DOUBLE,
# MAGIC     processed_time TIMESTAMP
# MAGIC   );
# MAGIC
# MAGIC INSERT INTO gerald_hopkins_workspace.default.prepared_songs
# MAGIC SELECT artist_id,
# MAGIC   artist_name,
# MAGIC   duration,
# MAGIC   release,
# MAGIC   tempo,
# MAGIC   time_signature,
# MAGIC   title,
# MAGIC   year,
# MAGIC   CURRENT_TIMESTAMP()
# MAGIC   FROM gerald_hopkins_workspace.default.songs_raw;
