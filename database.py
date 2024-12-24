import sqlite3
import importlib
db = sqlite3.connect('userss.db', check_same_thread = False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS userss(
    chatid TEXT,
    username TEXT,
    level INT
)""") 
db.commit()