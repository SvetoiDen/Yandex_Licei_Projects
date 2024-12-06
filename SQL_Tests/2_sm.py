import sqlite3

db = sqlite3.connect('strongmen.db')
cursor = db.cursor()
db.commit()

places = input().split()
found_trolles_name = set()
found_trolles_streng = 0
found_cnt = 0

for elem in places:
    try:
        trolles = cursor.execute(
            f"SELECT name, strength FROM Trolls WHERE strength >= 5 AND place = '{elem}'").fetchall()

        for row in trolles:
            found_trolles_name.add(row[0])
            found_trolles_streng += row[1]
            found_cnt += 1
    except Exception as e:
        continue

print(', '.join(sorted(found_trolles_name, key=lambda x: x[0])))
print(round(found_trolles_streng / found_cnt, 2))
