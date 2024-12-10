from datetime import datetime
import pandas as pd

def clean_data(df_pph: pd.DataFrame) -> pd.DataFrame:
    """Limpa e transforma os dados para adequação ao modelo.

    Args:
        df_pph (pd.DataFrame): [description]

    Returns:
        pd.DataFrame: [description]
    """
    # Remover de colunas não usadas
    df_pph = df_pph.drop(columns=['Plan', 'Device  Type', 'UPH', 'Buyer', 'PST', 'PET', 'Total', 'Result', 'Space'])  
    # Derreter colunas
    df_pph = pd.melt(
        df_pph,
        id_vars=['Org.', 'Model', 'Suffix'],
        var_name='Date',
        value_name='Quantity'
    )
    # Conversão de dados
    df_pph['Quantity'] = df_pph['Quantity'].astype(int)
    df_pph['Model.Suffix'] = df_pph['Model'] + '.' + df_pph['Suffix']
    df_pph = df_pph[['Model.Suffix', 'Org.', 'Date', 'Quantity']]

    # Ajuste de datas
    df_pph['Date'] = pd.to_datetime(df_pph['Date'].str.replace(r'^D[+-]\d+\s', '', regex=True).str.strip(), format='%d-%b', errors='coerce')
    current_year = datetime.now().year
    df_pph['Date'] = df_pph['Date'].apply(lambda x: x.replace(year=current_year if x.month >= datetime.now().month else current_year + 1))
    # Adição de 3 horas
    df_pph['Date'] = df_pph['Date'].apply(lambda x: x.replace(hour=3, minute=0, second=0))

    return df_pph
