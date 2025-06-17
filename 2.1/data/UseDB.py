import sqlite3
connect = sqlite3.connect('data/DataBase.db')
cursor = connect.cursor()
class Use_DB:
	def create_line(self, info):
		cursor.execute(f'''INSERT INTO info(name, value) VALUES('{info[0]}', '{info[1]}') ''')
		connect.commit()
	def update_line(self, name, info):
		cursor.execute(f'''UPDATE info SET value = '{info}' WHERE name = '{name}' ''')
		connect.commit()
	def read_line(self, name, id_):
		cursor.execute(f'''SELECT * FROM info WHERE name = '{name}' ''')
		data = cursor.fetchall()
		return data[0][2]
	def close_db(self):
		connect.close()
