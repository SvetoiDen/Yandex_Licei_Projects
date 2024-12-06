import sqlite3


def get_result(name):
    db = sqlite3.connect(name)
    cursor = db.cursor()
    db.commit()

    id1 = cursor.execute("SELECT id FROM genres WHERE title='фантастика'").fetchone()[0]

    cursor.execute(f"DELETE FROM films WHERE genre = {id1} AND year <= 2000 AND duration >= 90")
    db.commit()
