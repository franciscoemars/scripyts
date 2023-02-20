"""
Ex. Postgres
Criando Tabela e Adicionado dados
"""
import sqlalchemy as sqla
from sqlalchemy import create_engine, Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.orm import Session
from datetime import date

data_atual = date.today()

# Cria uma conexão com um banco de dados SQLite 
engine = create_engine(
    'postgresql://postgres:SENHA@192.168.0.0:5432/database')

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Cria uma classe que representa a tabela
Base = declarative_base()

class HistNumb(Base):
    __tablename__ = 'hist_numb'
    __table_args__ = {'schema': 'my_schema'} # Forte abraço ao ChatGPT!

    id = Column(Integer, primary_key=True)
    id_car = Column(Integer)
    placa = Column(String)
    numero = Column(String(3))
    created = Column(Date)

# Cria a tabela no banco de dados
# Base.metadata.create_all(engine)

# Adiciona dadados
'''
num_car = HistNumb(
    id_car=2, 
    placa='ZZZ1505',
    numero = '125',
    created = data_atual)
session.add(num_car)
session.commit()
'''

# Consultas
'''
query = session.query(HistNumb).filter_by(id=1)
resultado = query.first()
print(resultado.placa)
print(resultado.created)
'''