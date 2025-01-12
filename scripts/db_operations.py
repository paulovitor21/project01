from sqlalchemy.orm import Session
from scripts.models import BomRecord
from scripts.generate_hash import generate_hash

def save_to_db(df_bom, db: Session, file_date):
    """
    Salva os registros no banco de dados usando ORM.
    Processa todos os registros, mas apenas os registros não duplicados serão inseridos no banco.

    Args:
        df_pph (DataFrame): DataFrame com os dados a serem inseridos.
        db (Session): Sessão do banco de dados.
    """

    # Passo 1: Criar uma coluna 'temp_id' no DataFrame com números crescentes
    df_bom['temp_id'] = range(1, len(df_bom) + 1)

    # Passo 2: Gerar o hash baseado na combinação das colunas
    df_bom['hash_id'] = df_bom.apply(
        lambda row: generate_hash(row['temp_id']),
        axis=1
    )

    duplicate_count = 0  # Contador para duplicados
    inserted_count = 0  # Contador para registros inseridos
    for _, row in df_bom.iterrows():
        # Verificar se o hash já existe no banco
        exists = db.query(BomRecord).filter_by(hash_id=row['hash_id']).first()

        if exists:
            duplicate_count += 1  # Incrementa o contador de duplicados
            print(f"[Duplicado] Registro já existe para hash: {row['hash_id']}. Ignorando este registro.")
            continue  # Ignora a inserção do registro duplicado, mas continua processando os próximos
        
        # Se não for duplicado, criar e adicionar o novo registro
        record = BomRecord(
            file_date = file_date,
            org = row['org.'],
            top_item = row['top item'],
            child_item = row['child item'],
            child_desc = row['child desc'],
            child_uit = row['child uit'],
            qpa = row['qpa'],
            local = row['local'],
            assy = row['assy'],
            planner = row['planner'],
            purchaser = row['purchaser'],
            supplier = row['supplier'],
            supplier_name = row['supplier name'],
            model_mrp = row['model mrp'],
            infor = row['infor'],
            date = row['date'],
            quantity = row['quantity'],
            hash_id=row['hash_id']  # Usando o hash_id gerado
        )
        db.add(record)
        inserted_count += 1  # Incrementa o contador de registros inseridos

    # Commit no banco
    db.commit()
    # Exibe a quantidade de duplicados encontrados
    print(f"Total de duplicados encontrados: {duplicate_count}")
    print(f"Total de registros não duplicados inseridos: {inserted_count}")
    print("[Inserido] Todos os registros não duplicados foram inseridos com sucesso.")