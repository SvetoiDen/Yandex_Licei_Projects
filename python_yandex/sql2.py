import sqlite3

c1 = """
SELECT title FROM Films 
    WHERE genre IN ((
SELECT id FROM genres 
    WHERE title = 'музыка'),(
SELECT id FROM genres
    WHERE title='анимация')) AND year >= 1997
"""

bd_name = input()

db = sqlite3.connect(bd_name)
cursor = db.cursor()
db.commit()

for row in cursor.execute(c1).fetchall():
    print(row[1])
