import sqlite3


class SQLite_project():
    def __init__(self):
        self._sqlite = sqlite3.connect('./config/db_project.db')
        self._cursor = self._sqlite.cursor()

    def select_get(self, query: str):
        return self._cursor.execute(query).fetchone()

    def select_gets(self, query: str):
        return self._cursor.execute(query).fetchall()

    def commit_query(self, query: str):
        self._cursor.execute(query)
        self._sqlite.commit()

    def close(self):
        self._sqlite.close()
