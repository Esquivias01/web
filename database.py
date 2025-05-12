import pandas as pd
import sqlite3

# Nombre del archivo Excel y la hoja a leer
excel_file = 'pedido.csv'
#sheet_name = 'Hoja1'  # Cambia si tu hoja tiene otro nombre

df = pd.read_csv(excel_file)

sqlite_db = 'database.db'
table_name = 'pedidos'

conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print(f"El archivo '{excel_file}' ha sido importado a la base de datos '{sqlite_db}' en la tabla '{table_name}'.")

"""
# Nombre del archivo SQLite y la tabla
sqlite_db = 'database.db'
table_name = 'velas'

# Leer el archivo Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Conectar a la base de datos SQLite
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Crear la tabla automáticamente según las columnas del Excel
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Confirmar y cerrar la conexión
conn.commit()
conn.close()

print(f"El archivo '{excel_file}' ha sido importado a la base de datos '{sqlite_db}' en la tabla '{table_name}'.")
"""