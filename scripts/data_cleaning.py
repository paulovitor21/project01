from datetime import datetime
import pandas as pd

def clean_data(engine, df_delivery_status: pd.DataFrame) -> pd.DataFrame:
    """Limpa e transforma os dados para adequação ao modelo.

    Args:
        engine: Conexão ao banco de dados.
        df_delivery_status (pd.DataFrame): Dados a serem limpos.

    Returns:
        pd.DataFrame: Dados limpos e transformados.
    """
    # Limpar nomes das colunas
    df_delivery_status.columns = (
        df_delivery_status.columns
        .str.replace(r'[.\s-]', '_', regex=True)
        .str.lower()
    )

    # Converter a coluna 'receiving_1' para datetime e lidar com NaT
    if 'receiving_1' in df_delivery_status.columns:
        # Converter a coluna 'receiving_1' para datetime, forçando valores inválidos a se tornarem NaT
        df_delivery_status['receiving_1'] = pd.to_datetime(df_delivery_status['receiving_1'], errors='coerce')
    
    # Se necessário, lidar com valores NaT
    # Exemplo: substituir NaT por um valor específico, como uma data padrão
    df_delivery_status['receiving_1'].fillna(pd.Timestamp('1970-01-01'), inplace=True)


    # Garantir que colunas não datetime substituam NaN por None
    df_delivery_status = df_delivery_status.where(pd.notna(df_delivery_status), None)

    # Mapeamento de grupos
    group_mapping = {
        'NW1': 'TV', 'NWD': 'TV', 'NWH': 'TV', 'NWW': 'TV',
        'NW4': 'AV', 'NWU': 'AV', 'NWX': 'AV',
        'NW7': 'AC', 'NW8': 'AC', 'NWQ': 'AC',
        'NWK': 'BM'
    }

    # Adicionar coluna 'group'
    df_delivery_status['group'] = df_delivery_status['org'].map(group_mapping).fillna('Others')

    # Data de referência
    plan_pph_value = datetime.now()

    # Consulta para buscar a data mais recente do banco
    query = "SELECT date FROM table_pph_teste WHERE date >= %s"
    params = (plan_pph_value,)
    df_reference_date = pd.read_sql(query, engine, params=params)

    # Atualizar a data de referência
    if not df_reference_date.empty:
        plan_pph_value = df_reference_date['date'].max()

    # Adicionar a coluna 'Status' de forma vetorizada
    df_delivery_status['status'] = (
         (df_delivery_status['receiving_1'] == pd.Timestamp('1970-01-01')) | 
        (df_delivery_status['receiving_1'] >= plan_pph_value)
    ).map({True: 'Y', False: 'N'})

    return df_delivery_status
