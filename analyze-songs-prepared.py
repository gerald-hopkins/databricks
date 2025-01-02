# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM gerald_hopkins_workspace.default.prepared_songs LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT artist_name, count(artist_name) AS num_songs, year
# MAGIC FROM gerald_hopkins_workspace.default.prepared_songs
# MAGIC WHERE year > 0
# MAGIC GROUP BY artist_name, year
# MAGIC ORDER BY num_songs DESC, year DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM prepared_songs WHERE artist_name = 'Eric Clapton';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT artist_name,
# MAGIC   title,
# MAGIC   tempo
# MAGIC FROM prepared_songs
# MAGIC WHERE time_signature = 4
# MAGIC   AND tempo BETWEEN 100 AND 140;
