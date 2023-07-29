USE livraria;
CREATE TABLE cliente (
	cpf char(11) NOT NULL PRIMARY KEY,
    nome char(45),
    telefone char(11),
    email char(45)
    );
    

CREATE TABLE vendas (
	idevendas int not null primary key,
    cliente_cpf char(11),
    preco_total float,
    data datetime,
    foreign key (cliente_cpf) references cliente(cpf)
    );
    
create table editoras (
	ideditoras int not null primary key,
    nome char(45),
    endereco char(255),
    email char(45)
    );
    
create table livros (
	idlivros int not null primary key,
    titulo char(255),
    autor char(45),
    num_pag int,
    qnt_estoque int,
    preco_unid float,
    genero char(45),
    editoras_ideditoras int,
    foreign key (editoras_ideditoras) references editoras(ideditoras)
    );
    
    
alter table vendas change idevendas idvendas int; 

create table vendas_livros (
	idvendas_livros int not null primary key,
    vendas_idvendas int,
    livros_idlivros int,
    qnt_vendida int,
    foreign key (vendas_idvendas) references vendas(idvendas),
    foreign key (livros_idlivros) references livros(idlivros)
    );
    
use livraria;
ALTER TABLE cliente modify telefone char(14);
ALTER TABLE livraria.vendas drop foreign key vendas_ibfk_1;
ALTER TABLE cliente modify cpf char(14);
ALTER TABLE livraria.vendas add foreign key (cliente_cpf) references cliente(cpf);
ALTER TABLE vendas modify cliente_cpf char(14);
