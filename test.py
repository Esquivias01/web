import sqlite3


enf = 'Insomnio'
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute(f"SELECT * FROM pedidos")
query = c.fetchall()
conn.close()
print(query)