'''
Ex. Postgress
Script para Copiar objetos de uma tabela para outra.
Usado em producao (19/02/2023)
'''

from sqlalchemy import (
    create_engine, Table, Column, Integer, String, Date, MetaData, select, insert)
from datetime import date

data_atual = date.today()

# criar uma conexão com o banco de dados
engine = create_engine(
    'postgresql://postgres:senha@192.168.0.0:5432/banco')

# definir as tabelas com SQLAlchemy
metadata = MetaData(schema='my_schema')

origem = Table('veiculos', metadata,
    Column('id', Integer, primary_key=True),
    Column('placa', String),
    Column('numero', Integer),
)
destino = Table('hist_numb', metadata,
    Column('id_car', Integer),
    Column('placa', String),
    Column('numero', Integer),
    Column('created', Date)
)

# copiar os dados da tabela origem para a tabela destino
with engine.connect() as conexao:
    consulta = select([origem])
    resultados = conexao.execute(consulta)

    for linha in resultados:
        ins = destino.insert().values(
            placa=linha.placa,
            numero=linha.numero,
            id_car=linha.id,
            created=data_atual
        )
        conexao.execute(ins)
