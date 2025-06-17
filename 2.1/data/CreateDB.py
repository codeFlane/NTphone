import sqlite3

def Create_DB():
	connect = sqlite3.connect('data/DataBase.db')
	cursor = connect.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS info(
		id INTEGER PRIMARY KEY,
		name TEXT,
		value TEXT)''')
	connect.commit()
	connect.close
