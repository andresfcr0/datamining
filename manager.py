import sqlite3, json, datetime
from uuid import uuid4


class DAO:

    def __init__(self, *args, **kwargs):
        self.connection = sqlite3.connect("db.sqlite")
        self.cursor = self.connection.cursor()

    def createTables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                    id TEXT PRIMARY KEY, 
                    name TEXT, 
                    email TEXT
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS calculations (
                    id TEXT PRIMARY KEY, 
                    user_id TEXT,
                    results TEXT, 
                    date TEXT,
                    FOREIGN KEY(user_id) REFERENCES user(id)
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS outcome (
                    id TEXT PRIMARY KEY, 
                    calc_id TEXT,
                    outcome TEXT,
                    FOREIGN KEY(calc_id) REFERENCES calculations(id)
            )
            """
        )

        self.connection.commit()

    def insertCalculation(self, json_obj):
        user_id = json_obj["user_id"]
        del json_obj["user_id"]
        self.cursor.execute(
            f"""
            INSERT INTO calculations VALUES(
                '{uuid4()}', 
                '{user_id}',
                '{json.dumps(json_obj)}',
                '2024-03-01 16:22:22.082264'
            )
            """
            # '{datetime.datetime.now()}'
        )

        self.connection.commit()

    def selectCalculations(self):
        self.cursor.execute(
            f"""
            SELECT * FROM calculations
            WHERE CAST ((
                JulianDay('now') - JulianDay(date)
            ) As Integer) > 30
            """
        )

        return self.cursor.fetchall()
