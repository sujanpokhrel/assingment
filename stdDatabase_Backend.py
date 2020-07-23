import _sqlite3
#backend


def studentData():
    con= sqlite3.connect("student.db")
    cur.execute("CRETE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StDID, text, Firstname text, Surname text, DoB text, \
                Age text, Gender text, Address text, Mobile text")
