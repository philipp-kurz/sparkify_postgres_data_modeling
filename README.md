# Project overview
Because the executive suite of the imaginary music streaming startup Sparkify kept hearing that "data is the new oil in the 21st century", they decided to collect any data they could about the songs they offer and their users' listening activity.

However, the data was collected in the from of individual JSON files, and the startup quickly realized that its data analysts and scientists are having a hard time leveraging the data that way. Hence, the executives decided to bring a data engineer onto the team to make the data available in a relational PostgreSQL database instead.

I completed this project as part of the [Udacity Data Engineering nanodegree program](https://www.udacity.com/course/data-engineer-nanodegree--nd027).

# Analytical Goals
The analytics team has an interest in understanding which songs users are listening to and to which times they do so.

The main reasons are:
* Knowing how often songs from a specific artist were listened to is an important metric for paying song license fees to artists accordingly.
* Being aware of how many users are using their service at any given time of the day or the week allows Sparkify to plan server maintenances with the least impact on its users.
* Sparkify can analyze the songs that users are listening to in order to personalize their recommendations of new tracks for each of its users.

# Database Schema
The PostgreSQL database was modeled according to a Star schema, with the `songplays` table at its center. The schema is almost fully normalized, and the `songplays` table references the `songs` and `artists` tables which contain information about Sparkify's songs, as well as the `users` and `time` tables which store user and time information. The database schema is visualized below.

![Database Schema](sparkify_db_schema.png)

# ETL Pipeline

First, the `sparkifydb` PostgreSQL database has to be set up. To do so, the [create_tables.py](create_tables.py) script, as the name suggests, creates the database tables by utilizing the respective table creation queries found in [sql_queries.py](sql_queries.py).

# Sample Queries