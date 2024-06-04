import sqlite3 as sql

# Conectando ao banco de dados
con = sql.connect('form-db.db')
cur = con.cursor()

# Deletando a tabela 'tickets' se já existir
cur.execute('DROP TABLE IF EXISTS tickets')

# Criando a tabela 'tickets'
sql_create_table = '''
    CREATE TABLE "tickets" (
    "NF" INTEGER PRIMARY KEY NOT NULL,
    "DATA" TEXT NOT NULL,
    "PESO" REAL NOT NULL
    );
    '''

cur.execute(sql_create_table)

# Salvando as mudanças e fechando a conexão
con.commit()
con.close()
