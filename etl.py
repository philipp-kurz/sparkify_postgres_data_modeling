import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

# Needed so that np.int64 can be read by psycopg2
import numpy as np
from psycopg2.extensions import register_adapter, AsIs

def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)
    df = df.replace({np.nan: None})

    # insert song record
    cols = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = list(df[cols].iloc[0].values)
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    cols = ['artist_id', 'artist_name', 'artist_location', 
            'artist_latitude', 'artist_longitude']
    artist_data = list(df[cols].iloc[0].values)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)
    df = df.replace({np.nan: None})

    # filter by NextSong action
    df = df[df['page'] == 'NextSong'] 

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    t = df['ts']
    
    # insert time data records
    time_df = pd.DataFrame(t)
    time_df.columns = ['start_time']
    time_df['hour'] = time_df['start_time'].dt.hour
    time_df['day'] = time_df['start_time'].dt.day
    time_df['week'] = time_df['start_time'].dt.week
    time_df['month'] = time_df['start_time'].dt.month
    time_df['year'] = time_df['start_time'].dt.year
    time_df['weekday'] = time_df['start_time'].dt.weekday

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    cols = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[cols]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, 
                         row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    all_files = [file for file in all_files if file.find('.ipynb') == -1]

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    register_adapter(np.float64, addapt_numpy_float64)
    register_adapter(np.int64, addapt_numpy_int64)
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()