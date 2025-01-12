import pandas as pd
import numpy as np


def clean_data(engine, df_bom: pd.DataFrame) -> pd.DataFrame:
    """Limpa e transforma os dados para adequação ao modelo.

    Args:
        engine: Conexão ao banco de dados.
        df_bom (pd.DataFrame): Dados a serem limpos.

    Returns:
        pd.DataFrame: Dados limpos e transformados.
    """
    
    # Manter as colunas
    columns_to_keep = ['Org.', 'Top Item', 'Child Item', 'Child Desc', 'Child UIT', 'QPA', 
                       'LOCAL', 'Assy', 'Planner', 'Purchaser', 'Supplier', 
                       'Supplier Name', 'Model MRP']

    df_bom = df_bom[columns_to_keep]
    
    # Transformar os nomes das colunas para minúsculas
    df_bom.columns = df_bom.columns.str.lower()

    # Aplicar o filtro na coluna 'child uit' e fazer uma cópia do resultado
    criterios = ["M", "P", "R", "T", "G"]
    df_bom = df_bom[df_bom['child uit'].isin(criterios)].copy()

    # Converter colunas para string
    df_bom.loc[:, 'child item'] = df_bom['child item'].astype(str)
    df_bom.loc[:, 'child desc'] = df_bom['child desc'].astype(str)
    df_bom.loc[:, 'child uit'] = df_bom['child uit'].astype(str)

    # Converter para float64 explicitamente na coluna 'qpa'
    df_bom.loc[:, 'qpa'] = pd.to_numeric(df_bom['qpa'], errors='coerce')  # Garantir que erros sejam convertidos para NaN
    
    # Convertendo outras colunas para string
    df_bom.loc[:, 'local'] = df_bom['local'].astype(str)
    df_bom.loc[:, 'assy'] = df_bom['assy'].astype(str)
    df_bom.loc[:, 'planner'] = df_bom['planner'].astype(str)
    df_bom.loc[:, 'purchaser'] = df_bom['purchaser'].astype(str)
    df_bom.loc[:, 'supplier'] = df_bom['supplier'].astype(str)
    df_bom.loc[:, 'supplier name'] = df_bom['supplier name'].astype(str)
    df_bom.loc[:, 'model mrp'] = df_bom['model mrp'].astype(str)

    # Criar a coluna 'Infor' e preencher com o valor 'Plano'
    df_bom['infor'] = 'Plano'

    try:
        # Query para selecionar as colunas 'Date' e 'Quantity' de sua tabela
        sql_query = "SELECT date, quantity FROM table_pph_teste"
    
        # Passar a consulta para o pandas
        df_reference_data = pd.read_sql(sql_query, engine)

        # Verifique se os dados foram retornados corretamente
        print(df_reference_data.head())  # Exibe as primeiras linhas de df_reference_data

        # Verifique a quantidade de linhas de df_reference_data
        print(f"Número de linhas em df_reference_data: {len(df_reference_data)}")
        
        # Verifique se há valores nulos nas colunas
        print(df_reference_data.isnull().sum())

        # Adicionar as colunas 'date' e 'quantity'
        df_bom['date'] = df_reference_data['date']
        df_bom['quantity'] = df_reference_data['quantity']
        
        # Garantir que o número de linhas seja igual em ambos os DataFrames
        # if len(df_bom) == len(df_reference_data):
        #     # Adicionar as colunas 'date' e 'quantity'
        #     df_bom['date'] = df_reference_data['date']
        #     df_bom['quantity'] = df_reference_data['quantity']
        # else:
        #     print("Aviso: O número de linhas em df_bom e df_reference_data não coincide!")

    except Exception as e:
        print(f"Erro ao executar a consulta SQL: {e}")
    
    df_bom = df_bom.replace({np.nan: None})
    
    return df_bom

