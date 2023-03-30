import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_speedcamera_sql = """
   -- speedcamera table
   CREATE TABLE IF NOT EXISTS speedcamera (
      id integer PRIMARY KEY,
      latitude REAL NOT NULL,
      longitude REAL NOT NULL,
      status text NOT NULL
   );
   """

   create_description_sql = """
   -- description table
   CREATE TABLE IF NOT EXISTS description (
      id integer PRIMARY KEY,
      speedcamera_id integer NOT NULL,
      latitude REAL NOT NULL,
      longitude REAL NOT NULL,
      speed_limit INTEGER NOT NULL,
      type TEXT NOT NULL,
      direction TEXT NOT NULL,
      survey_date text NOT NULL,
      FOREIGN KEY (speedcamera_id) REFERENCES speedcamera (id)
   );
   """
 
   db_file = "fotoradar.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_speedcamera_sql)
       execute_sql(conn, create_description_sql)
       conn.close()