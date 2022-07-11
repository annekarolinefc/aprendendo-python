#BIBLIOTECA PSYCOPG2
import psycopg2

#CONFIGURAÇÕES
#UPDATE CONNECTION STRING INFORMATION
host = 'localhost'
dbname = 'test'
user = 'postgres'
password = 'postgres'
sslmode = 'require'

#STRING DE CONEXAO
#CONSTRUCT CONNECTION STRING
conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
print(conn_string)

#Abrindo a conexao com o banco
#conn = psycopg2.connect(conn_string)
conn = psycopg2.connect("dbname=teste user=postgres password=postgres")
print('Connection established')

#CURSOR: cara que ira executar os comandos
cursor = conn.cursor()

#EXISTE A TABELA USUARIOS COM ID, NOME, EMAIL E SENHA
#CRIAR TABELA #CREATE TABLE
'''
cursor.execute('CREATE TABLE usuarios( id serial PRIMARY KEY, nome VARCHAR(50), email VARCHAR(50), senha VARCHAR(50))')
print('Finished creating table')
'''
#CRUD
#comando = ''
#cursor.execute(comando)
#conexao.commit() -> quando edita o banco de dados
#resultado=cursor.fetchall() -> ler o banco de dados


#CREATE
#comando = 'INSERT INTO nome-tabela(col1, col2, col3) VALUES (val1, val2, val3)'
def create_user(nome, email, senha):
    cursor.execute("INSERT INTO usuarios(nome, email, senhar) VALUES(%s, %s, %s);", (nome, email, senha))

create_user('NOVO USUARIO', 'USUARIO@GMAIL.COM', '123456')
cursor.commit() #editar o banco de dados

#EXIBIR
def find_all():
    cursor.execute('SELECT * FROM usuarios;')
    return cursor.fetchall()

users = find_all()
print(users)

#PESQUISAR UM USUARIO ESPECIFICO
def find_one(id):
    cursor.execute("SELECT * FROM usuarios WHERE id=%s;", (id,))
    return cursor.fetchall()

#ATUALIZAR
def update_user(id, nome, email, senhar):
    cursor.execute("UPDATE usuarios SET nome=%s, email=%s, senhar=%s WHERE id=%s;", (nome, email, senhar, id))

update_user(5, "Anne", "anne@gmail.com", "123456")

#DELETAR
def delete_user(id):
    cursor.execute('DELETE FROM usuarios WHERE id=%s;', (id,))
#comitar alteração
conn.commit()

user = find_one(2)
print(user)
delete_user(8)

#FECHAR O CURSOS E A CONEXAO
cursor.close()
conn.close()