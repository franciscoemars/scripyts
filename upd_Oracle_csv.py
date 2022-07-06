"""
Script basico para importar dados de um csv para o banco
@femars
"""
import cx_Oracle
import pandas as pd

# Import CSV
data = pd.read_csv (r'RBP1.csv')   
df = pd.DataFrame(data)

# Conexao com o banco (Oracle)
connection = cx_Oracle.connect(user="p11", password='zecomeia',
                               dsn="192.168.0.1:1539/protheustst")
cursor = connection.cursor()

for row in df.itertuples():
    cursor.execute("UPDATE SA1010 SET A1_VEND = 'RBTL16' WHERE TRIM(A1_COD||A1_LOJA) =""'"+row.CODIGO+"'")
    print(row.CODIGO) # CODIGO = Coluna
    connection.commit()

connection.close()