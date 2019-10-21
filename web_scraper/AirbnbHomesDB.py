import sqlite3
import os

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), 'airbnb_homes.sqlite3')

class AirbnbHomesDB(object):
    """
    This class is responsible for all database functions related to executing and analyzing lighthouse audits
    """
    def __init__(self, db_path=DEFAULT_DB_PATH):
        """
        Constructor
        """
        print(db_path)
        self.db_path = db_path # path of the database file
        self.initialize()

    def initialize(self):
        """Create the results table if it doesn't exist"""
        table_sql = """CREATE TABLE IF NOT EXISTS HOMES (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TITLE text,
                        URL text,
                        IMAGE_LINK text)"""
        try:
            connection = self.connect()
            cur = connection.cursor()
            cur.execute(table_sql)
            connection.close()
        except Exception as err:
            print("DB Initializing failed.", err) 

    def connect(self):
        """create a database connection """
        try:
            con = sqlite3.connect(self.db_path)
        except:
            print("Database connection failed.")
        return con
    
    def save(self, title, url, image_link):
        """save the LighthouseAudit object"""
        insert_sql = """INSERT INTO HOMES (
                        title, 
                        url, 
                        image_link)
                        VALUES (?,?,?)
                    """
        try:
            connection = self.connect()
            cur = connection.cursor()
            # create values tuple that could be passed to sql execution command
            values_tuple = (title, url, image_link)
            cur.execute(insert_sql, values_tuple)
            connection.commit()
            connection.close()
        except:
            print("Database save failed.")

    def getAllRecords(self):
        """return all records in the results table"""
        select_sql = "SELECT * FROM HOMES"
        return self.getRecords(select_sql)

    def getRecords(self, sql_statement):
        """return records based on the sql_statement parameter"""
        try:
            connection = self.connect()
            cur = connection.cursor()
            cur.execute(sql_statement)
            rows = cur.fetchall()
            connection.close()
        except Exception as e:
            print("Database select failed.", e)
        return rows
    
    def get_random_home(self):
      select_sql = "SELECT title, image_link FROM homes ORDER BY RANDOM() LIMIT 1;"
      return self.getRecords(select_sql)[0]
    
    def get_random_home_image(self):
      select_sql = "SELECT image_link FROM homes ORDER BY RANDOM() LIMIT 1;"
      return self.getRecords(select_sql)[0][0]
       
if __name__ == '__main__':
    ab = AirbnbHomesDB()
    pass
