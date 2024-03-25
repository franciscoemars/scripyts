"""
Script para atualizar determinados campos do banco de dados baseado em uma planilha do tipo Excel XLSX.

Importante!  Conexão do Banco já deve estar breviamente configurada.
Exemplo utilizando Banco de Dados Oracle.


femars - 25/03/2024
"""
import sqlalchemy as sqla
import pandas as pd
import traceback

# Conexao com o banco (Oracle)
prod = sqla.create_engine(
    'oracle+cx_oracle://p11:P11@192.168.1.3/protheusprod')

tst = sqla.create_engine(
    'oracle+cx_oracle://p11:P11@192.168.1.4/protheustst', echo=True)

orcl = prod

# Planilha no formato EXCEL
bruta = pd.read_excel(r'vendedores_inativos.xlsx')

# Query a ser executado 
upd = """UPDATE SA1010
        SET A1_VEND = :alteracao
        WHERE 
            A1_COD = :cod
        AND A1_LOJA = :loja """

# UPDATE
with orcl.connect() as conn: # Conexao com o banco
    for row in bruta.itertuples(): # Leitura da planilha por linhas
        try:
            print(f'Atualizando Registro: {row.A1_COD}{row.A1_LOJA} - {row.Alterar}')
            # Execucao do Update 
            update = conn.execute(sqla.text(upd).params(alteracao=row.Alterar, cod=row.A1_COD, loja=row.A1_LOJA))
            conn.commit()
        except Exception as e:
            traceback.print_exc()