from sqlalchemy.orm import Session
from scripts.models import PPHRecord
from scripts.generate_hash import generate_hash

def save_to_db(df_pph, db: Session):
    """
    Salva os registros no banco de dados usando ORM.
    Processa todos os registros, mas apenas os registros não duplicados serão inseridos no banco.

    Args:
        df_pph (DataFrame): DataFrame com os dados a serem inseridos.
        db (Session): Sessão do banco de dados.
    """
    duplicate_count = 0  # Contador para duplicados
    inserted_count = 0  # Contador para registros inseridos
    for _, row in df_pph.iterrows():
        # Gerar o hash do registro
        record_hash = generate_hash(row['Model.Suffix'], row['Org.'], row['Date'])
        
        # Verificar se o hash já existe no banco
        exists = db.query(PPHRecord).filter_by(hash=record_hash).first()
        
        if exists:
            duplicate_count += 1  # Incrementa o contador de duplicados
            print(f"[Duplicado] Registro já existe para hash: {record_hash}. Ignorando este registro.")
            continue  # Ignora a inserção do registro duplicado, mas continua processando os próximos
        
        # Se não for duplicado, criar e adicionar o novo registro
        record = PPHRecord(
            model_suffix=row['Model.Suffix'],
            org=row['Org.'],
            date=row['Date'],
            quantity=row['Quantity'],
            hash=record_hash
        )
        db.add(record)
        inserted_count += 1  # Incrementa o contador de registros inseridos

    # Commit no banco
    db.commit()
    # Exibe a quantidade de duplicados encontrados
    print(f"Total de duplicados encontrados: {duplicate_count}")
    print(f"Total de registros não duplicados inseridos: {inserted_count}")
    print("[Inserido] Todos os registros não duplicados foram inseridos com sucesso.")



# from sqlalchemy.orm import Session
# from scripts.models import PPHRecord
# from scripts.generate_hash import generate_hash

# def save_to_db(df_pph, db: Session):
#     """Salvar os registros no banco de dados usando ORM.

#     Args:
#         df_pph ([type]): [description]
#         db (Session): [description]
#     """
#     for _, row in df_pph.iterrows():
#         # Gerar o hash do registro
#         record_hash = generate_hash(row['Model.Suffix'], row['Org.'], row['Date'])
#         # Verificar se o hash já existe no banco
#         exists = db.query(PPHRecord).filter_by(hash=record_hash).first()
#         if exists:
#             print(f"[Duplicado] Registro já existe para hash: {record_hash}. Processamento interrompido.")
#             return False  # Indica que a inserção não foi realizada

#         if not exists:
#             record = PPHRecord(
#                 model_suffix = row['Model.Suffix'],
#                 org = row['Org.'],
#                 date = row['Date'],
#                 quantity = row['Quantity'],
#                 hash=record_hash
#             )
#             db.add(record)
#     db.commit()
#     print(f"[Inserido] Registro inserido com sucesso para hash: {record_hash}.")
#     return True  # Indica que a inserção foi bem-sucedida