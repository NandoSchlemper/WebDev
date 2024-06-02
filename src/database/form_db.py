import sqlite3 as sql

# Conectando ao banco de dados
con = sql.connect('form-db.db')
cur = con.cursor()

# Deletando a tabela 'users' se já existir
cur.execute('DROP TABLE IF EXISTS users')

# Criando a tabela 'users'
sql_create_table = '''
    CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "USERNAME" TEXT NOT NULL,
    "AGE" INT
    );
    '''

cur.execute(sql_create_table)

# Salvando as mudanças e fechando a conexão
con.commit()
con.close()
