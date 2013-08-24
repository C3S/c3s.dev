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

class ExploitationPayoutCalculationRule(Base):

    __tablename__ = 'exploitationpayoutcalculationrule'
    Rule = Column(String,index = True, primary_key = True)
    Username = Column(String, ForeignKey('accountant.Username'), nullable = True)
    invoiceitem_id = Column(Integer, ForeignKey('exploitationpayout.invoiceitem_id'), nullable = True)

class ExploitationPayout(InvoiceItem):

    __mapper_args__ = {'polymorphic_identity':'exploitationpayout'}
    invoiceitem_id = Column(Integer, ForeignKey('invoiceitem.invoiceitem_id'),primary_key = True)
    __tablename__ = 'exploitationpayout'