from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint

Base = declarative_base()

class PPHRecord(Base):
    """AI is creating summary for PPHRecord

    Args:
        Base ([type]): [description]
    """
    __tablename__= 'table_pph_teste'

    id = Column(Integer, primary_key=True, index=True)
    model_suffix = Column(String, index=True)
    org = Column(String)
    date = Column(DateTime)
    quantity = Column(Integer)
    hash = Column(String, unique=True)

    __table_args__ = (
        UniqueConstraint('hash', name='unique_hash_constraint'),  # Garantir unicidade
    )
