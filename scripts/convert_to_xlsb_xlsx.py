import pandas as pd

def convert_xlsb_to_xlsx(xlsb_file, xlsx_file):
    """
    Converte um arquivo .xlsb para .xlsx.
    """
    try:
        # Ler o arquivo .xlsb usando pandas e pyxlsb
        data = pd.read_excel(xlsb_file, engine='pyxlsb')

        # Salvar o DataFrame como .xlsx
        data.to_excel(xlsx_file, index=False)
        print(f"Arquivo convertido com sucesso: {xlsx_file}")
    except Exception as e:
        print(f"Erro ao converter arquivo: {e}")
        raise