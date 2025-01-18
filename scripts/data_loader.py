import pandas as pd

def load_excel(file_path: str) -> pd.DataFrame:
    """Carregar arquivo excel para retornar um Dataframe

    Args:
        file_path (str): [description]

    Returns:
        pd.DataFrame: [description]
    """
    xls = pd.ExcelFile(file_path)
    df_bom = xls.parse(header=0)
    return df_bom