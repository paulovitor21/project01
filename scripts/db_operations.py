from sqlalchemy.orm import Session
from scripts.models import BomRecord
import logging

def save_to_db(df_bom, db: Session, file_date):
    """
    Salva os registros no banco de dados usando ORM.
    Processa todos os registros de um arquivo, mas apenas insere os registros
    caso a data do arquivo não esteja presente no banco.

    Args:
        df_bom (DataFrame): DataFrame com os dados a serem inseridos.
        db (Session): Sessão do banco de dados.
        file_date (str): Data do arquivo a ser processado.

    Returns:
        bool: True se novos registros foram inseridos, False caso contrário.
    """
    # Verificar se já existem registros no banco para a mesma data do arquivo
    existing_records = db.query(BomRecord).filter_by(file_date=file_date).first()
    if existing_records:
        logging.info(f"[Ignorado] Registros para a data {file_date} já existem no banco. Nenhum registro foi inserido.")
        return False  # Nenhum dado foi inserido

    # Inserir os registros, pois não existem registros para a data do arquivo
    inserted_count = 0
    for _, row in df_bom.iterrows():
        record = BomRecord(
            file_date=file_date,
            org=row['org.'],
            top_item=row['top item'],
            child_item=row['child item'],
            child_desc=row['child desc'],
            child_uit=row['child uit'],
            qpa=row['qpa'],
            local=row['local'],
            assy=row['assy'],
            planner=row['planner'],
            purchaser=row['purchaser'],
            supplier=row['supplier'],
            supplier_name=row['supplier name'],
            model_mrp=row['model mrp'],
            infor=row['infor'],
            date=row['date'],
            quantity=row['quantity'],
        )
        db.add(record)
        inserted_count += 1

    # Commit no banco
    db.commit()

    # Exibir mensagem de sucesso apenas se registros forem inseridos
    logging.info(f"[Inserido] Total de registros inseridos para a data {file_date}: {inserted_count}.")
    logging.info("Dados salvos com sucesso!")
    return True
