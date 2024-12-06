import sqlite3


def yourself(db, *args):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    db.commit()

    found_member = []

    for row in args:
        try:
            t1 = cursor.execute(
                f"SELECT place_id, master_id, alien FROM Events WHERE kindness = -1 AND alien = '{row}'").fetchall()
            for elem in t1:
                hoz = cursor.execute(f"SELECT surname FROM Masters WHERE id = {elem[1]}").fetchone()[0]
                place = cursor.execute(f"SELECT place FROM Places WHERE id = {elem[0]}").fetchone()[0]
                found_member.append((hoz, place, elem[2]))
        except Exception:
            continue

    db.close()
    r = sorted(set(found_member), key=lambda x: (x[0], sorted(x[2], reverse=True)), reverse=True)
    return r
