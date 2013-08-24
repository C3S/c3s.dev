# -*- coding: utf-8 -*-
from c3s.dev.accountancy.invoicing import InvoiceItem
from c3s.dev.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class UtilisationFeeCalculationRule(Base):

    __tablename__ = 'utilisationfeecalculationrule'
    Rule = Column(String,index = True, primary_key = True)
    invoiceitem_id = Column(Integer, ForeignKey('utilisationfee.invoiceitem_id'), nullable = True)
    Username = Column(String, ForeignKey('accountant.Username'), nullable = True)
    ucontext_id = Column(Integer, ForeignKey('utilisation_context.ucontext_id'), nullable = True)

class UtilisationFee(InvoiceItem):

    __mapper_args__ = {'polymorphic_identity':'utilisationfee'}
    invoiceitem_id = Column(Integer, ForeignKey('invoiceitem.invoiceitem_id'),primary_key = True)
    __tablename__ = 'utilisationfee'
    utilisationPayout_invoiceitem_id = Column(Integer, ForeignKey('exploitationpayout.invoiceitem_id'), nullable = True)