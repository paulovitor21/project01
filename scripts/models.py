from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Double, DateTime, UniqueConstraint

Base = declarative_base()

class DeliveryRecord(Base):
    """AI is creating summary for PPHRecord

    Args:
        Base ([type]): [description]
    """
    __tablename__= 'table_delivery_status_teste'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    group = Column(String)
    org = Column(String)
    item = Column(String)
    uit = Column(String)
    delivery_type = Column(String)
    supplier_code = Column(String)
    name = Column(String)
    departure_no = Column(String)
    inspection_flag = Column(String)
    po = Column(Integer)
    po_remain = Column(Integer)
    departure = Column(Integer)
    departure_cancel = Column(Integer)
    arrival = Column(Integer)
    arrival_cancel = Column(Integer)
    iqc_status = Column(String)
    receiving = Column(Integer)
    po_no = Column(String)
    kanban_code = Column(Double)
    work_order = Column(String)
    line = Column(String)
    po_subinventory = Column(String)
    po_locator = Column(Double)
    po_creation = Column(String)
    po_due = Column(String)
    departure_1 = Column(String)
    departure_cancel_1 = Column(String)
    arrival_1 = Column(String)
    arrival_cancel_1 = Column(String)
    iqc_judgement = Column(String)
    receiving_1 = Column(DateTime)
    planner = Column(String)
    uom = Column(String)
    purchaser = Column(String)
    w_keeper = Column(String)
    desc = Column(String)
    spec = Column(String)
    item_cost = Column(String)
    po_currency_code = Column(String)
    po_price = Column(String)
    wms_item = Column(String)
    departure_2 = Column(String)
    departure_cancel_2 = Column(String)
    arrival_2 = Column(String)
    arrival_cancel_2 = Column(String)
    receiving_2 = Column(String)
    nota_no = Column(String)


    # __table_args__ = (
    #     UniqueConstraint('hash', name='unique_hash_constraint'),  # Garantir unicidade
    # )
