import os
import logging
from scripts.db_connection import SessionLocal, engine
from scripts.models import Base
from scripts.data_loader import load_excel
from scripts.data_cleaning import clean_data
from scripts.db_operations import save_to_db
from scripts.convert_to_xlsb_xlsx import convert_xlsb_to_xlsx
import pandas as pd
from datetime import datetime

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extrair_data(file_path):
    data_criacao = os.path.getctime(file_path)
    data_criacao_formatada = datetime.fromtimestamp(data_criacao).strftime('%Y-%m-%d %H:%M:%S')
    return data_criacao_formatada

def main():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Criar sessão
    db = SessionLocal()

    try:
        # Caminho do arquivo .xlsb de origem e arquivo convertido
        xlsb_file = r"C:\Users\Paulo\Downloads\Downloads-1\1210_Bom_Master.xlsb"
        #xlsb_file = r"C:\Users\Paulo\Documents\data_g\ref\1213_Bom_Master.xlsb"
        #sheet_name = "BOM_Master"
        xlsx_file = "bom.xlsx"
        
        convert_xlsb_to_xlsx(xlsb_file, xlsx_file)
        
        # Carregar os dados
        file_path = xlsx_file
        #sheet_name = sheet_name
        df_bom = load_excel(file_path)

        # Extrair data do arquivo
        file_date = extrair_data(file_path)
        logging.info(f"Data do ARQUIVO -> {file_date}")
        
        # Limpar os dados
        df_bom = clean_data(engine, df_bom)

        # Salvar no banco
        save_to_db(df_bom, db, file_date)
        logging.info("Dados salvos com sucesso!")

    except Exception as e:
        # Imprimir mais informações sobre o erro
        logging.error(f"Ocorreu um erro na execução do processo: {e}")
        logging.exception("Detalhes do erro: ")

    finally:
        db.close()

if __name__ == "__main__":
    main()
