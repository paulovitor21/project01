from sqlalchemy.orm import Session
from scripts.models import DeliveryRecord
from scripts.generate_hash import generate_hash



def save_to_db(df_delivery_status, db: Session):
    """
    Salva os registros no banco de dados usando ORM.
    Processa todos os registros, mas apenas os registros não duplicados serão inseridos no banco.

    Args:
        df_pph (DataFrame): DataFrame com os dados a serem inseridos.
        db (Session): Sessão do banco de dados.
    """
    # Passo 1: Criar uma coluna 'temp_id' no DataFrame com números crescentes
    df_delivery_status['temp_id'] = range(1, len(df_delivery_status) + 1)

    # Passo 2: Gerar o hash baseado na combinação das colunas
    df_delivery_status['hash_id'] = df_delivery_status.apply(
        lambda row: generate_hash(row['temp_id'], row['status'], row['group'], row['item'], row['arrival_1']),
        axis=1
    )

    duplicate_count = 0  # Contador para duplicados
    inserted_count = 0  # Contador para registros inseridos
    for _, row in df_delivery_status.iterrows():
        # Verificar se o hash já existe no banco
        exists = db.query(DeliveryRecord).filter_by(hash_id=row['hash_id']).first()

        if exists:
            duplicate_count += 1  # Incrementa o contador de duplicados
            print(f"[Duplicado] Registro já existe para hash: {row['hash_id']}. Ignorando este registro.")
            continue  # Ignora a inserção do registro duplicado, mas continua processando os próximos
        
        # Se não for duplicado, criar e adicionar o novo registro
        record = DeliveryRecord(
            status=row['status'],
            group=row['group'],
            org=row['org'],
            item=row['item'],
            uit=row['uit'],
            delivery_type=row['delivery_type'],
            supplier_code=row['supplier_code'],
            name=row['name'],
            departure_no=row['departure_no'],
            inspection_flag=row['inspection_flag'],
            po=row['po'],
            po_remain=row['po_remain'],
            departure=row['departure'],
            departure_cancel=row['departure_cancel'],
            arrival=row['arrival'],
            arrival_cancel=row['arrival_cancel'],
            iqc_status=row['iqc_status'],
            receiving=row['receiving'],
            po_no=row['po_no'],
            kanban_code=row['kanban_code'],
            work_order=row['work_order'],
            line=row['line'],
            po_subinventory=row['po_subinventory'],
            po_locator=row['po_locator'],
            po_creation=row['po_creation'],
            po_due=row['po_due'],
            departure_1=row['departure_1'],
            departure_cancel_1=row['departure_cancel_1'],
            arrival_1=row['arrival_1'],
            arrival_cancel_1=row['arrival_cancel_1'],
            iqc_judgement=row['iqc_judgement'],
            receiving_1=row['receiving_1'],
            planner=row['planner'],
            uom=row['uom'],
            purchaser=row['purchaser'],
            w_keeper=row['w_keeper'],
            desc=row['desc'],
            spec=row['spec'],
            item_cost=row['item_cost'],
            po_currency_code=row['po_currency_code'],
            po_price=row['po_price'],
            wms_item=row['wms_item'],
            departure_2=row['departure_2'],
            departure_cancel_2=row['departure_cancel_2'],
            arrival_2=row['arrival_2'],
            arrival_cancel_2=row['arrival_cancel_2'],
            receiving_2=row['receiving_2'],
            nota_no=row['nota_no'],
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
