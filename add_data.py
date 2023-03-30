
import sqlite3

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: fotoradar file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_speedcamera(conn, speedcamera):
   """
   Create a new speedcamera into the speedcamera table
   :param conn:
   :param speedcamera:
   :return: speedcamera id
   """
   sql = '''INSERT INTO speedcamera(latitude, longitude, status)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, speedcamera)
   conn.commit()
   return cur.lastrowid

def add_description(conn, description):
   """
   Create a new description into the description table
   :param conn:
   :param description:
   :return: speedcamera id
   """
   sql = '''INSERT INTO description(speedcamera_id, latitude, longitude, speed_limit, type, direction, survey_date)
             VALUES(?,?,?,?,?,?,?)''' 
   cur = conn.cursor()
   cur.execute(sql, description)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   speedcamera = ("53.49236", "18.76033","Surveyed")

   conn = create_connection("fotoradar.db")
   sp_id = add_speedcamera(conn, speedcamera)

   description = (
       sp_id,
       "53.49236",
       "18.76033",
       "50",
       "Fixed",
       "N",
       "2020-05-11",
   )

   description_id = add_description(conn, description)

   print(sp_id, description_id)
   conn.commit()