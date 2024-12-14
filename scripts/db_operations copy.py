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
    duplicate_count = 0  # Contador para duplicados
    inserted_count = 0  # Contador para registros inseridos
    for _, row in df_delivery_status.iterrows():
        # Gerar o hash do registro
        record_hash = generate_hash(row['id'], row['status'], row['group'], row['item'], row['arrival_1'])
        
        #Verificar se o hash já existe no banco
        exists = db.query(DeliveryRecord).filter_by(hash_id=record_hash).first()
        
        if exists:
            duplicate_count += 1  # Incrementa o contador de duplicados
            print(f"[Duplicado] Registro já existe para hash: {record_hash}. Ignorando este registro.")
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
            hash_id=record_hash
        )
        db.add(record)
        inserted_count += 1  # Incrementa o contador de registros inseridos

    # Commit no banco
    db.commit()
    #Exibe a quantidade de duplicados encontrados
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