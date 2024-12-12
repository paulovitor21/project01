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
        file_path = r"C:\Users\Paulo\Documents\project01\data\Delivery Status 12042024 0833.xlsx"
        sheet_name = 'Sheet1'
        df_delivery_status = load_excel(file_path, sheet_name)
    
        # Limpar os dados
        df_delivery_status = clean_data(engine, df_delivery_status)

        # Salvar no banco
        save_to_db(df_delivery_status, db)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()