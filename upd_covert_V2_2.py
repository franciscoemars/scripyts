import sqlalchemy as sqla
import pandas as pd
import traceback

# Conexao com o banco (Oracle)
prod = sqla.create_engine(
    'oracle+cx_oracle://p11:P11@192.168.1.3/protheusprod')

tst = sqla.create_engine(
    'oracle+cx_oracle://p11:P11@192.168.1.4/protheustst')

orcl = prod

# Planilha no formato EXCEL
bruta = pd.read_excel(r'Pasta1.xlsx')

# Query a ser executado 
# CD2010
upd_cd2 = """UPDATE CD2010
    SET CD2_BC = 0
        ,CD2_ALIQ = 0
        ,CD2_VLTRIB = 0
    WHERE 
        CD2_FILIAL = '02'
        AND D_E_L_E_T_ = ' '
        AND CD2_IMP = 'ICM'
        AND CD2_DOC LIKE :doc
        AND CD2_CODFOR LIKE :forne"""
# SD1
upd_sd1 = """UPDATE SD1010 
    SET D1_VALICM = 0
        ,D1_PICM = 0
        ,D1_BASEICM = 0 
    WHERE 
        D1_FILIAL = '02'
        AND D1_DOC LIKE :doc
        AND D1_FORNECE LIKE :forne"""
# SF1
udp_sf1 = """UPDATE SF1010
    SET F1_BASEICM = 0
        ,F1_VALICM = 0
    WHERE
        F1_FILIAL = '02'
        AND F1_DOC LIKE :doc
        AND F1_FORNECE LIKE :forne"""

# UPDATE
with orcl.connect() as conn: # Conexao com o banco
    for row in bruta.itertuples(): # Leitura da planilha por linhas
        try:
            print(f'Atualizando Registro: {row.DOC} - {row.FORNEC}')
            # Adiciona o caractere coringa '%' aos parâmetros
            doc_param = f"%{row.DOC}"
            forne_param = f"%{row.FORNEC}"
            # Execucao do Update 
            result_cd2 = conn.execute(sqla.text(upd_cd2).params(doc=doc_param, forne=forne_param))
            result_sd1 = conn.execute(sqla.text(upd_sd1).params(doc=doc_param, forne=forne_param))
            result_sf1 = conn.execute(sqla.text(udp_sf1).params(doc=doc_param, forne=forne_param))
            
            # Verifica se alguma linha foi atualizada
            if result_cd2.rowcount > 0 or result_sd1.rowcount > 0 or result_sf1.rowcount > 0:
                print(f'Registro {row.DOC} - {row.FORNEC} atualizado com sucesso.')
            else:
                print(f'Nenhuma atualização econtrada para o registro {row.DOC} - {row.FORNEC}.')
            
        except Exception as e:
            traceback.print_exc()
