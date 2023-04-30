import mysql.connector
from faker import Faker

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gabriela1",
  database="Livraria"
)

cursor = conexao.cursor()

sql = "INSERT INTO editoras (ideditoras, nome, endereco, email) VALUES (%s, %s, %s, %s)"

valores = []
nome_editoras = [
    'Companhia das Letras',
    'Record',
    'Sextante',
    'Intrínseca',
    'Rocco',
    'Objetiva',
    'Planeta',
    'Zahar',
    'Aleph',
    'Jangada',
    'Novo Conceito',
    'Suma de Letras',
    'Arqueiro',
    'Vida & Consciência',
    'Gente',
    'Belas-Letras',
    'Martins Fontes',
    'Escala',
    'Moderna',
    'Alta Books'
]

fk = Faker('pt_BR')

for i in range(20):
  ideditoras = i+1
  nome = nome_editoras[i]
  endereco = fk.address()
  email = f"{nome}@gmail.com"
  email = email.replace(" ","").lower()
  valores.append((ideditoras, nome, endereco, email))

for valor in valores:
  cursor.execute(sql, valor)

conexao.commit()

cursor.execute("SELECT * FROM editoras")

resultados = cursor.fetchall()

for resultado in resultados:
  print(resultado)