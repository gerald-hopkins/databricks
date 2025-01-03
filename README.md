Databricks Songs Data Engineering Sample

In this repo, you'll find my code to use in Databricks notebooks to:

- connect to the Databricks onboard out-of-the-box music sample dataset
- profile the data for schema and transformations
- use a spark stream with Databricks Autoloader to load the data into a raw delta table (stream-load-songs.py)
- create a prepared table and load data into it (prepare-songs-data.py)
- analyze the data (analyze-songs-prepared.py)
- practice creating delta tables with SQL and querying them (tables-practice.py)

