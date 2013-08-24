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

class MembershipFeeCalculationRule(Base):

    __tablename__ = 'membershipfeecalculationrule'
    Rule = Column(String,index = True, primary_key = True)

class MembershipFee(InvoiceItem):

    __mapper_args__ = {'polymorphic_identity':'membershipfee'}
    invoiceitem_id = Column(Integer, ForeignKey('invoiceitem.invoiceitem_id'),primary_key = True)
    __tablename__ = 'membershipfee'
    Rule = Column(String, ForeignKey('membershipfeecalculationrule.Rule'), nullable = True)