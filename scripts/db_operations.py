from sqlalchemy.orm import Session
from scripts.models import PPHRecord

def save_to_db(df_pph, db: Session):
    """Salvar os registros no banco de dados usando ORM.

    Args:
        df_pph ([type]): [description]
        db (Session): [description]
    """
    for _, row in df_pph.iterrows():
        record = PPHRecord(
            model_suffix = row['Model.Suffix'],
            org = row['Org.'],
            date = row['Date'],
            quantity = row['Quantity']
        )
        db.add(record)
    db.commit()