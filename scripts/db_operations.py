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
        #record_hash = generate_hash(row['Model.Suffix'], row['Org.'], row['Date'])
        
        # Verificar se o hash já existe no banco
        #exists = db.query(PPHRecord).filter_by(hash=record_hash).first()
        
        # if exists:
        #     duplicate_count += 1  # Incrementa o contador de duplicados
        #     print(f"[Duplicado] Registro já existe para hash: {record_hash}. Ignorando este registro.")
        #     continue  # Ignora a inserção do registro duplicado, mas continua processando os próximos
        
        # Se não for duplicado, criar e adicionar o novo registro
        record = DeliveryRecord(
            status=row['Status'],
            group=row['Group'],
            org=row['ORG'],
            item=row['Item'],
            uit=row['UIT'],
            delivery_type = row['Delivery Type'],
            supplier_code = row['Supplier Code'],
            name = row['Name'],
            departure_no = row['Departure No'],
            inspection_flag = row['Inspection Flag	'],
            po = row['PO'],
            po_remain = row['PO Remain'],
            departure = row['Departure'],
            departure_cancel = row['Departure Cancel'],
            arrival = row['Arrival'],
            arrival_cancel = row['Arrival Cancel'],
            iqc_status = row['IQC Status'],
            receiving = row['Receiving'],
            po_no = row['PO No'],
            kanban_code = row['Kanban Code'],
            work_order = row['Work Order'],
            line = row['Line'],
            po_subinventory = row['PO Subinventory'],
            po_locator = row['PO Locator'],
            po_creation = row['PO Creation'],
            po_due = row['PO Due'],
            departure_1 = row['Departure.1'],
            departure_cancel_1 = row['Departure Cancel.1'],
            arrival_1 = row['Arrival.1'],
            arrival_cancel_1 = row['Arrival Cancel.1'],
            iqc_judgement = row['IQC Judgement'],
            receiving_1 = row['Receiving.1'],
            planner = row['Planner'],
            uom = row['Uom'],
            purchaser = row['Purchaser'],
            w_keeper = row['W-Keeper'],
            desc = row['Desc'],
            spec = row['Spec'],
            item_cost = row['Item Cost'],
            po_currency_code = row['Po Currency Code'],
            po_price = row['Po Price'],
            wms_item = row['WMS Item'],
            departure_2 = row['Departure.2'],
            departure_cancel_2 = row['Departure Cancel.2'],
            arrival_2 = row['Arrival_2'],
            arrival_cancel_2 = row['Arrival Cancel.2'],
            receiving_2 = row['Receiving.2'],
            nota_no = row['Nota No']
            #hash=record_hash
        )
        db.add(record)
        inserted_count += 1  # Incrementa o contador de registros inseridos

    # Commit no banco
    db.commit()
    # Exibe a quantidade de duplicados encontrados
    # print(f"Total de duplicados encontrados: {duplicate_count}")
    # print(f"Total de registros não duplicados inseridos: {inserted_count}")
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