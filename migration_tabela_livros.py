import random
import mysql.connector
from faker import Faker

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gabriela1",
  database="Livraria"
)

cursor = conexao.cursor()

sql = "INSERT INTO livros (idlivros, titulo, autor, num_pag, qnt_estoque, preco_unid, genero, editoras_ideditoras) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

valores = []

titulos = ['A Hora da Estrela', 'A Cabana', 'O Sol é para Todos', 'O Senhor dos Anéis', 'As Crônicas de Nárnia', '1984',
           'O Pequeno Príncipe', 'A Menina que Roubava Livros', 'Dom Casmurro', 'Memórias Póstumas de Brás Cubas',
           'O Grande Gatsby', 'A Revolução dos Bichos', 'Cem Anos de Solidão', 'O Hobbit', 'O Apanhador no Campo de Centeio',
           'Harry Potter e a Pedra Filosofal', 'O Leão, a Feiticeira e o Guarda-Roupa', 'Os Miseráveis', 'A Culpa é das Estrelas',
           'Morte Súbita', 'O Nome do Vento', 'O Código Da Vinci', 'Os Pilares da Terra', 'As Vinhas da Ira', 'O Poderoso Chefão',
           'A Sombra do Vento', 'O Príncipe', 'O Retrato de Dorian Gray', 'O Conde de Monte Cristo', 'O Morro dos Ventos Uivantes',
           'O Médico e o Monstro', 'O Processo', 'A Revolta de Atlas', 'A Bíblia Sagrada', 'A Montanha Mágica', 'O Silmarillion',
           'Crime e Castigo', 'A Divina Comédia', 'O Perfume', 'O Velho e o Mar', 'Guerra e Paz', 'O Vermelho e o Negro',
           'O Despertar dos Mágicos', 'O Caçador de Pipas', 'O Lobo da Estepe', 'A Arte da Guerra', 'O Alquimista',
           'A Terra Desolada', 'O Homem que Calculava', 'O Jardim Secreto', 'A Ilha do Tesouro', 'As Aventuras de Tom Sawyer',
           'A Revolução dos Bichos', 'A Menina do Vale', 'A Coragem de Ser Imperfeito', 'O Ódio que Você Semeia',
           'A Origem das Espécies', 'A História de um Milagre', 'A História de uma Alma', 'A Insustentável Leveza do Ser',
           'A Livraria Mágica de Paris', 'A Maldição do Titã', 'A Mão Esquerda de Deus', 'A Menina que Roubava Cerejas',
           'A Menina que Tinha Dons', 'A Moreninha', 'A Mulher na Janela', 'A Noiva Fantasma', 'A Nuvem', 'A Odisseia',
           'A Ordem do Tempo', 'A Passageira', 'A Pequena Princesa', 'A Princesa Prometida', 'A Rainha Vermelha',
           'A Razão doa Pais', 'A Revolução dos Bichos em Quadrinhos', 'A Sereia', 'A Sociedade Literária e a Torta de Casca de Batata',
           'A Trégua', 'A Vida de David Gale', 'A Vida Mentirosa dos Adultos', 'A Vida Secreta das Abelhas',
           'Água para Elefantes', 'Além do Bem e do Mal', 'Algoritmos para Viver', 'Amor nos Tempos de Cólera', 'Anjo Mecânico',
           'Anna Karenina', 'Antes que Eu Vá', 'Arquivos do Semideus', 'As Aventuras de Alice no País das Maravilhas',
           'As Aventuras de Sherlock Holmes', 'As Cidades Invisíveis', 'As Vantagens de Ser Invisível', 'As Viagens de Gulliver',
           'Atlas Shrugged', 'Auto da Compadecida', 'Beleza Negra', 'Belgravia', 'Bird Box', 'Black Hammer',
           'Brilho Eterno de uma Mente sem Lembranças', 'Cabeça de Papel', 'Café Society', 'Capitães da Areia', 'Cemitério Maldito',
           'Chapeuzinho Amarelo', 'Chapeuzinho Vermelho', 'Cidades de Papel', 'Clube da Luta', 'Comer, Rezar, Amar',
           'Conversations with Friends', 'Coração de Tinta', 'Crônicas de gelo e fogo', 'Daisy Jones & The Six', 'Deuses Americanos',
           'Dezesseis Luas', 'Diário de Anne Frank', 'Duna', 'E Não Sobrou Nenhum', 'E o Vento Levou', 'Eleanor Oliphant está muito bem',
           'Emma', 'Ensaio sobre a Cegueira', 'Entrevista com o Vampiro', 'Era dos Extremos', 'Esperando Godot', 'Estação Onze',
           'Eu Sou o Mensageiro', 'Extremamente Alto e Incrivelmente Perto', 'Fahrenheit 451', 'Falando o Mais Rápido que Posso',
           'Fallen', 'Frankenstein', 'Geração de Valor', 'Girl, Interrupted', 'Guerra dos Tronos', 'Hannibal', 'Heidi', 'Hellblazer',
           'Hibisco Roxo', 'Histórias Extraordinárias', 'Homem-Aranha: Entre Trovões', 'Homo Deus', 'Hotel Transilvânia',
           'House of Leaves', 'Howl', 'Identidade Bourne', 'Ilíada', 'Incidente em Antares', 'Inferno', 'Inferno no Colégio Interno',
           'Infinite Jest', 'Insaciável', 'Into the Wild', 'Jane Eyre', 'Jogos Vorazes', 'Johnny Bleas', 'Jonathan Livingston Seagull',
           'Journey to the Center of the Earth', 'Júlio César', 'Jurassic Park', 'Just Kids', 'Kafka à Beira-Mar', 'Ladrão de Almas',
           'Le Chevalier D’Eon', 'Legend', 'Leite Derramado', 'Livre', 'Lolita', 'Lone Wolf and Cub', 'Longitude', 'Luz em Agosto',
           'Machado de Assis: Contos Completos', 'Mágico de Oz', 'Malcolm X', 'Mansfield Park', 'Marley e Eu', 'Maus', 'Memórias de um Sargento de Milícias', 'Mentes Perigosas', 'Mensagem', 'Middlesex', 'Milagre na Rua 34',
           'Uma Breve História do Tempo', 'Uma Noite na Praia', 'Um Estranho Numa Terra Estranha', 'Um Lugar Bem Longe Daqui',
           'Um Lugar Chamado Notting Hill', 'Um Milhão de Finais Felizes', 'Um Mundo Brilhante', 'Um Olhar do Paraíso','O alquimista',
           'Um Perfeito Cavalheiro', 'Um Porto Seguro', 'Um Quarto Próprio', 'Um Teto Todo Seu', 'Um Toque de Vermelho',
           'Uncharted: O Quarto Labirinto', 'V de Vingança', 'Vamos Juntas?', 'Vampiros de Morganville', 'Véu da Verdade',
           'Viagem ao Centro da Terra', 'Viagem ao Redor do Meu Quarto', 'Vidas Secas', 'Vingança Mortal', 'Vinte Mil Léguas Submarinas',
           'Violetas de Março', 'Vira-lata de Raça', 'Viver Depois de Ti', 'Viver é Ridículo', 'Viver para Contar', 'Viver Sem Depressão',
           'Watchmen', 'What I Talk About When I Talk About Running', 'Where the Sidewalk Ends', 'White Oleander', 'Winnie-the-Pooh',
           'Wuthering Heights', 'Xeque-mate', 'X-Men: A Saga da Fênix Negra', 'Y: O Último Homem', 'You Are a Badass',
           'Z: A Cidade Perdida', 'Zen e a Arte da Manutenção de Motocicletas', 'Zero a Um', 'Zoo', '1984','A sombra do vento',]

generos = ['Romance', 'Ficção científica', 'Mistério', 'Suspense', 'Fantasia', 'Drama', 'Não-ficção', 'Biografia', 'Histórico', 'Autoajuda']

fk = Faker('pt_BR')

for i in range(231):
  idlivros = i+1
  titulo = titulos[i]
  autor = fk.name()
  num_pag = random.randint(200,500)
  qnt_estoque = random.randint(0,100)
  preco_unid = random.uniform(49,230)
  preco_unid = round(preco_unid, 2)
  genero = generos[random.randint(0,9)]
  editoras_ideditoras = random.randint(1,20)
  valores.append((idlivros, titulo, autor, num_pag, qnt_estoque, preco_unid, genero, editoras_ideditoras))

for valor in valores:
  cursor.execute(sql, valor)

conexao.commit()

cursor.execute("SELECT * FROM livros")

resultados = cursor.fetchall()

for resultado in resultados:
  print(len(resultado))