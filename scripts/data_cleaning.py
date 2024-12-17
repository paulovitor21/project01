from datetime import datetime
import pandas as pd

def clean_data(engine, df_bom: pd.DataFrame) -> pd.DataFrame:
    """Limpa e transforma os dados para adequação ao modelo.

    Args:
        engine: Conexão ao banco de dados.
        df_delivery_status (pd.DataFrame): Dados a serem limpos.

    Returns:
        pd.DataFrame: Dados limpos e transformados.
    """
    
    # manter as colunas
    columns_to_keep = ['Org.', 'Child Item', 'Child Desc', 'Child UIT', 'QPA', 
                   'LOCAL', 'Assy', 'Planner', 'Purchaser', 'Supplier', 
                   'Supplier Name', 'Model MRP']

    df_bom = df_bom[columns_to_keep]
    # Transforma os nomes das colunas para minúsculas
    df_bom.columns = df_bom.columns.str.lower()

    df_bom['child item'] = df_bom['child item'].astype(str)
    df_bom['child desc'] = df_bom['child desc'].astype(str)
    df_bom['child uit'] = df_bom['child uit'].astype(str)
    df_bom['qpa'] = df_bom['qpa'].astype(str)
    df_bom['local'] = df_bom['local'].astype(str)
    df_bom['assy'] = df_bom['assy'].astype(str)
    df_bom['planner'] = df_bom['planner'].astype(str)
    df_bom['purchaser'] = df_bom['purchaser'].astype(str)
    df_bom['supplier'] = df_bom['supplier'].astype(str)
    df_bom['supplier name'] = df_bom['supplier name'].astype(str)
    df_bom['model mrp'] = df_bom['model mrp'].astype(str)
    

    
    df_bom['Infor'] = 'Plano'

    # Query para selecionar as colunas 'Date' e 'Quantity' de sua tabela
    sql_query = """
        SELECT Date, Quantity
        FROM table_pph_teste
    """

    # Passar a consulta e o parâmetro para o pandas
    df_reference_data = pd.read_sql(sql_query, engine)

    df_bom['date'] = df_reference_data['date']
    df_bom['quantity'] = df_reference_data['quantity']
    
    return df_bom