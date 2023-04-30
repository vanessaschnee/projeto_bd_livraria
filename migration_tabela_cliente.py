import mysql.connector
from faker import Faker

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gabriela1",
  database="Livraria"
)

cursor = conexao.cursor()

sql = "INSERT INTO cliente (nome, cpf, email, telefone) VALUES (%s, %s, %s, %s)"

fk = Faker('pt_BR')

valores = []

for i in range(50):
  nome = fk.name()
  cpf = fk.cpf()
  email = f"{nome}@gmail.com"
  email = email.replace(" ","").lower()
  telefone = fk.phone_number()
  valores.append((nome, cpf, email, telefone))

for valor in valores:
  cursor.execute(sql, valor)

conexao.commit()

cursor.execute("SELECT * FROM cliente")

resultados = cursor.fetchall()

for resultado in resultados:
  print(resultado)