# -*- coding: utf-8 -*-
from c3s.dev.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class CollectingSociety(Base):

    __tablename__ = 'collectingsociety'
    society_id = Column(Integer,index = True, primary_key = True)
    invoice_id = Column(Integer, ForeignKey('invoice.invoice_id'), nullable = True)