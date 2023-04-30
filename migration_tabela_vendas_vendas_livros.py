import random
import datetime
import mysql.connector
from faker import Faker

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gabriela1",
  database="Livraria"
)

fk = Faker('pt_BR')

cursor = conexao.cursor()
query1 = "SELECT cpf FROM cliente"
query2 = "SELECT idlivros, titulo, preco_unid FROM livros"

cursor.execute(query1)
lista_cpf = cursor.fetchall()

cursor.execute(query2)
lista_livros = cursor.fetchall()

vendas = []

for i in range(0, 500):
    iniciodata = datetime.datetime(2023, 1, 1, 0, 0, 0)
    finaldata = datetime.datetime(2023, 4, 4, 23, 59, 59)

    vendas.append({
        "idvendas": i + 1,
        "cliente_cpf":  lista_cpf[random.randint(0,49)][0],
        "data": fk.date_time_between(start_date=iniciodata, end_date=finaldata),
        "preco_total": 0,
        "livros": []
    })

    quantidade_livros = random.randint(1, 3)

    for j in range(quantidade_livros):
        id_livro = lista_livros[random.randint(0,229)][0]
        preco = lista_livros[id_livro][2]
        vendas[i]['preco_total'] += preco
        vendas[i]['livros'].append({
            'livros_idlivros': id_livro
        })

query_inserir_vendas = "INSERT INTO vendas (idvendas, cliente_cpf, preco_total, data) VALUES (%s, %s, %s, %s)"
query_inserir_vendas_livros = "INSERT INTO vendas_livros (vendas_idvendas, livros_idlivros) VALUES (%s, %s)"

for venda in vendas:
    cursor.execute(query_inserir_vendas,
        (
            venda["idvendas"],
            venda["cliente_cpf"],
            venda["preco_total"],
            venda["data"],
        )
    )

    conexao.commit()

    for livro in venda['livros']:
        cursor.execute(query_inserir_vendas_livros,
            (
                venda["idvendas"],
                livro["livros_idlivros"]
            )
        )

        conexao.commit()