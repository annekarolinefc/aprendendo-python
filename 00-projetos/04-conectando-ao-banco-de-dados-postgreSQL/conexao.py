#BIBLIOTECA PSYCOPH2
# pip install psycopg2-binary
import psycopg2

#CONFIGURAÇÕES
#UPDATE CONNECTION STRING INFORMATION
host = 'localhost'
dbname = 'teste'
user = 'postgres'
password = 'postgres'
sslmode = 'require'

#STRING DE CONEXAO
#CONSTRUCT CONNECTION STRING
conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
print(conn_string)
#Abrindo a conexao com o banco
conn = psycopg2.connect(conn_string)
print('Connection established')

#CURSOR
cursor = conn.cursor()

#CRIAR TABELA
#CREATE TABLE
cursor.execute('CREATE TABLE inventory( id serial PRIMARY KEY, nome VARCHAR(50), quantity INT)')
print('Finished creating table')

#comitar alteração
conn.commit()
cursor.close()
#fechar conexao
conn.close()