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

    # Aplicar o filtro na coluna 'child uit' e faz uma cópia do resultado
    criterios = ["M", "P", "R", "T", "G"]
    df_bom = df_bom[df_bom['child uit'].isin(criterios)].copy()

    # Converter colunas para string
    df_bom = df_bom.astype({
        'child item': 'str', 'child desc': 'str', 'child uit': 'str', 
        'local': 'str', 'assy': 'str', 'planner': 'str', 
        'purchaser': 'str', 'supplier': 'str', 'supplier name': 'str', 
        'model mrp': 'str'
    })

    # Converter para float64 explicitamente na coluna 'qpa'
    df_bom.loc[:, 'qpa'] = pd.to_numeric(df_bom['qpa'], errors='coerce')

    # Criar a coluna 'infor' e preencher com o valor 'Plano'
    df_bom['infor'] = 'Plano'

    try:
        # Query para selecionar as colunas 'date' e 'quantity' de sua tabela
        sql_query = "SELECT date, quantity FROM table_pph_teste"
    
        # Passar a consulta para o pandas
        df_reference_data = pd.read_sql(sql_query, engine)

        # Adicionar as colunas 'date' e 'quantity'
        df_bom['date'] = df_reference_data['date']
        df_bom['quantity'] = df_reference_data['quantity']
        
    except Exception as e:
        print(f"Erro ao executar a consulta SQL: {e}")
    
    '''
    Se a coluna [local] for "Intern" ou "OSP", define o valor da coluna [infor] com o texto "Plano" seguido do número de vezes que a combinação de valores nas colunas ['org.', 'child item', 'assy'] apareceu até aquela linha.
    Se a coluna [local] não for "Intern" ou "OSP", define o valor da célula na coluna [infor] apenas com o texto "Plano".
    '''
    mask = df_bom['local'].isin(['Intern', 'OSP'])
    df_bom.loc[mask, 'infor'] = 'Plano' + (df_bom.loc[mask].groupby(['org.', 'child item', 'assy']).cumcount() + 1).astype(str)
    
    df_bom = df_bom.replace({np.nan: None})
    
    return df_bom
