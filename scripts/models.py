from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP

Base = declarative_base()

class BomRecord(Base):
    
    __tablename__= 'table_bom_teste'

    id = Column(Integer, primary_key=True, index=True)
    org = Column(name='org', type_=String)
    child_item = Column(name="child_item", type_=String)
    child_desc = Column(name="child_desc", type_=String)
    child_uit = Column(name="child_uit", type_=String)
    qpa = Column(name="qpa", type_=String)
    local = Column(name="local", type_=String)
    assy = Column(name="assy", type_=String)
    planner = Column(name="planner", type_=String)
    purchaser = Column(name="purchaser", type_=String)
    supplier = Column(name="supplier", type_=String)
    supplier_name = Column(name="supplier_name", type_=String)
    model_mrp = Column(name="model_mrp", type_=String)
    infor = Column(name="infor", type_=String)
    date = Column(name="date", type_=TIMESTAMP)
    quantity = Column(name="quantity", type_=Integer)
    hash_id = Column(String, unique=True)

