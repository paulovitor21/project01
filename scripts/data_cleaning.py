from datetime import datetime
import pandas as pd

def clean_data(engine, df_delivery_status: pd.DataFrame) -> pd.DataFrame:
    """Limpa e transforma os dados para adequação ao modelo.

    Args:
        df_pph (pd.DataFrame): [description]

    Returns:
        pd.DataFrame: [description]
    """
    # Converta a coluna 'Receiving.1' para datetime
    df_delivery_status['Receiving.1'] = pd.to_datetime(df_delivery_status['Receiving.1'], errors='coerce')
    
    # adição da colunas 'status' and 'group'
    df_status_group = pd.DataFrame({
        'Status': [''] * len(df_delivery_status),  # Inicializando com valores vazios, ou você pode adicionar valores específicos
        'Group': [''] * len(df_delivery_status),   # Inicializando com valores vazios
    })

    df_delivery_status = pd.concat([df_status_group, df_delivery_status], axis=1)

    # lista de grupos
    groups = [
        (['NW1', 'NWD', 'NWH', 'NWW'], 'TV'),
        (['NW4', 'NWU', 'NWX'], 'AV'),
        (['NW7', 'NW8', 'NWQ'], 'AC'),
        (['NWK'], 'BM')
    ]

    # adicionar grupos de acordo com a lista
    def add_group(item):
        for condition, group in groups:
            if item in condition:
                return group
        return 'Others'  # Caso não atenda a nenhuma das condições

    # Aplicar a função para preencher a coluna 'Group'
    df_delivery_status['Group'] = df_delivery_status['ORG'].apply(add_group)

    # Passo 1: Definir a data de referência como a data atual
    plan_pph_value = datetime.now()  # Pega a data atual como referência

    # Adicionar 'Status' -> Y or N
    # Passo 2: Ajustar a consulta SQL
    query = """
    SELECT date
    FROM table_pph_teste 
    WHERE date >= %s
    """
    # Passo 3: Definir os parâmetros como uma lista de tuplas
    params = (plan_pph_value, )
    # Passo 4: Passar a consulta e o parâmetro corretamente para o pandas
    df_reference_date = pd.read_sql(query, engine, params=params)
    # Passo 5: Se tiver alguma data correspondente, pega a mais recente
    if not df_reference_date.empty:
        plan_pph_value = df_reference_date['date'].max()  # Pegando a data mais recente

    # Função para calcular o valor da coluna 'Status' com base na data de referência dinâmica
    def calculate_status(row):
        # Verifica se 'Receiving.1' é vazio ou maior/igual ao valor de 'plan_pph_value'
        if pd.isna(row['Receiving.1']) or row['Receiving.1'] >= plan_pph_value:
            return 'Y'
        else:
            return 'N'

    # Passo 7: Adiciona a coluna 'Status' no DataFrame df_delivery_status
    df_delivery_status['Status'] = df_delivery_status.apply(lambda row: calculate_status(row), axis=1)

    return df_delivery_status
