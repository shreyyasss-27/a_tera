import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'password123'))
conn.commit()
conn.close()