from scripts.db_connection import SessionLocal, engine
from scripts.models import Base
from scripts.data_loader import load_excel
from scripts.data_cleaning import clean_data
from scripts.db_operations import save_to_db

def main():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Criar sessão
    db = SessionLocal()
    
    try:
        # Carregar os dados
        #file_path = r"C:\Users\Paulo\Documents\project01\referencia (1)\referencia\data_09_12_24\PPH Daily 12.09.2024.xlsx"
        file_path = r"C:\Users\Paulo\Documents\project01\referencia (1)\referencia\PPH Daily 12.04.2024.xlsx"
        df_pph = load_excel(file_path)
    
        # Limpar os dados
        df_pph = clean_data(df_pph)

        # Salvar no banco
        save_to_db(df_pph, db)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()