from scripts.db_connection import SessionLocal, engine
from scripts.models import Base
from scripts.data_loader import load_excel
from scripts.data_cleaning import clean_data
from scripts.db_operations import save_to_db
import pandas as pd
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

    
        # Limpar os dados
        df_bom = clean_data(engine, df_bom)
        print("Saida\n",df_bom.columns)

        # Salvar no banco
        save_to_db(df_bom, db)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()