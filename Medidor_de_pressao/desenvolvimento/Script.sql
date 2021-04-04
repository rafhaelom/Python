----- Criacao da tabela registro -----
create table registro (
	id serial not null,
	datahora timestamp,
	nome varchar(30),
	peso real,
	sistolica integer,
	diastolica integer,
	pulsacao integer,
	primary key (id)
);

----- Consulta da tabela -----
select * from registro;

