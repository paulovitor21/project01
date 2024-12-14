from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()

class DeliveryRecord(Base):
    """Modelo de DeliveryRecord para inserção no banco de dados utilizando SQLAlchemy ORM"""

    __tablename__ = 'table_delivery_status'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)  # Status
    group = Column(String)  # Group
    org = Column(String)  # Org
    item = Column(String)  # Item
    uit = Column(String)  # UIT
    delivery_type = Column(String)  # Delivery Type
    supplier_code = Column(String)  # Supplier Code
    name = Column(String)  # Name
    departure_no = Column(String)  # Departure No
    inspection_flag = Column(String)  # Inspection Flag
    po = Column(Integer)  # PO
    po_remain = Column(Integer)  # PO Remain
    departure = Column(Integer)  # Departure
    departure_cancel = Column(Integer)  # Departure Cancel
    arrival = Column(Integer)  # Arrival 1 (alterado de TIMESTAMP para Integer)
    arrival_cancel = Column(Integer)  # Arrival Cancel 1 (alterado de TIMESTAMP para Integer)
    iqc_status = Column(String)  # IQC Status
    receiving = Column(Integer)  # Receiving
    po_no = Column(String)  # PO No
    kanban_code = Column(Float)  # Kanban Code
    work_order = Column(String)  # Work Order
    line = Column(String)  # Line
    po_subinventory = Column(String)  # PO Subinventory
    po_locator = Column(Float)  # PO Locator
    po_creation = Column(String)  # PO Creation
    po_due = Column(String)  # PO Due
    departure_1 = Column(String)  # Departure 1
    departure_cancel_1 = Column(String)  # Departure Cancel 1
    arrival_1 = Column(String)  # Arrival 1
    arrival_cancel_1 = Column(String)  # Arrival Cancel 1
    iqc_judgement = Column(String)  # IQC Judgement
    receiving_1 = Column(DateTime)  # Receiving 1
    planner = Column(String)  # Planner
    uom = Column(String)  # UOM
    purchaser = Column(String)  # Purchaser
    w_keeper = Column(String)  # W-Keeper
    desc = Column(String)  # Desc
    spec = Column(String)  # Spec
    item_cost = Column(String)  # Item Cost
    po_currency_code = Column(String)  # PO Currency Code
    po_price = Column(String)  # PO Price
    wms_item = Column(String)  # WMS Item
    departure_2 = Column(String)  # Departure 2
    departure_cancel_2 = Column(String)  # Departure Cancel 2
    arrival_2 = Column(String)  # Arrival 2
    arrival_cancel_2 = Column(String)  # Arrival Cancel 2
    receiving_2 = Column(String)  # Receiving 2
    nota_no = Column(String)  # Nota No
    hash_id = Column(String, unique=True)

    # __table_args__ = (
    #     UniqueConstraint('hash_id', name='unique_hash_constraint'),  # Garantir unicidade
    # )
