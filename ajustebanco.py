import sqlite3

# conectando...
conn = sqlite3.connect('dadosjuliana.db')
# definindo um cursor
cursor = conn.cursor()

# # criando a tabela (schema)
# cursor.execute("CREATE TABLE dados (quantidade TEXT, sujeito TEXT, acessorio TEXT, acao TEXT, com TEXT )")

# cursor.execute("DELETE FROM dados WHERE quantidade = 8")

# cursor.execute('SELECT acao FROM dados WHERE acao IS NOT NULL ORDER BY RANDOM()')
cursor.execute('update dados set acao = null where acao =""')
cursor.execute('SELECT acao FROM dados WHERE acao IS NOT NULL ORDER BY RANDOM()')
a = cursor.fetchone()

print(a)


conn.commit()

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
