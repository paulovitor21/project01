import os
import logging
from scripts.db_connection import SessionLocal, engine
from scripts.models import Base
from scripts.data_loader import load_excel
from scripts.data_cleaning import clean_data
from scripts.db_operations import save_to_db
import pandas as pd
from datetime import datetime

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extrair_data(file_path):
    data_modificacao = os.path.getmtime(file_path)
    data_arquivo = datetime.fromtimestamp(data_modificacao).strftime('%Y-%m-%d')
    return data_arquivo

def main():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Criar sessão
    db = SessionLocal()

    try:
        # Carregar os dados
        file_path = r"C:\Users\Paulo\Documents\project01\data\1213_Bom_Master.xlsx"
        sheet_name = 'BOM_Master'
        df_bom = load_excel(file_path, sheet_name)

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
