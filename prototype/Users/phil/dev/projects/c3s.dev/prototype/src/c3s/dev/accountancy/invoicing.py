# -*- coding: utf-8 -*-
from c3s.dev.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class InvoiceItem(Base):

    __tablename__ = 'invoiceitem'
    discriminator = Column(String)
    __mapper_args__ = {'polymorphic_on':discriminator}
    invoiceitem_id = Column(Integer,index = True, primary_key = True)
    invoice_id = Column(Integer, ForeignKey('invoice.invoice_id'), nullable = True)

class Invoice(Base):

    __tablename__ = 'invoice'
    invoice_id = Column(Integer,index = True, primary_key = True)
    Rule = Column(String, ForeignKey('membershipfeecalculationrule.Rule'), nullable = True)
    invoicereceiver_id = Column(Integer, ForeignKey('invoicereceiver.invoicereceiver_id'), nullable = True)

class InvoiceReceiver(Base):

    __tablename__ = 'invoicereceiver'
    discriminator = Column(String)
    __mapper_args__ = {'polymorphic_on':discriminator}
    invoicereceiver_id = Column(Integer,index = True, primary_key = True)