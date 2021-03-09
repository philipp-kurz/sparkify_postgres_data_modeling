# DROP TABLES

songplay_table_drop = ""
user_table_drop = ""
song_table_drop = ""
artist_table_drop = ""
time_table_drop = ""

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id int PRIMARY KEY,
                                start_time timestamp with time zone NOT NULL,
                                user_id int NOT NULL,
                                level text,
                                song_id text NOT NULL,
                                artist_id text NOT NULL,
                                session_id text NOT NULL,
                                location text,
                                user_agent text                         
                                )
                            """)

user_table_create = (""" CREATE TABLE IF NOT EXSITS users (
                            user_id int PRIMARY KEY,
                            first_name text NOT NULL,
                            last_name text NOT NULL,
                            gender text,
                            level text               
                            )
                        """)

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (
                            song_id text PRIMARY KEY,
                            title text NOT NULL,
                            artist_id text NOT NULL,
                            year int,
                            duration numeric                            
                            )
                        """)

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
                            artist_id text PRIMARY KEY,
                            name text NOT NULL,
                            location text,
                            latitude numeric,
                            longitude numeric
                            )
                        """)

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (
                        start_time timestamp with timezone,
                        hour int,
                        day int,
                        week int,
                        month int,
                        year int,
                        weekday text
                        )
                    """)

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]