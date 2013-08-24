# -*- coding: utf-8 -*-
from c3s.dev.user_management import User
from c3s.dev.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class Utiliser(User):

    __mapper_args__ = {'polymorphic_identity':'utiliser'}
    Username = Column(String, ForeignKey('user.Username'),primary_key = True)
    __tablename__ = 'utiliser'
    Name = Column(String)
    ucontext_id = Column(Integer, ForeignKey('utilisation_context.ucontext_id'), nullable = True)

class Utilisation(Base):

    __tablename__ = 'utilisation'
    Date_time = Column(String)
    utilisation_id = Column(Integer,index = True, primary_key = True)
    invoiceitem_id = Column(Integer, ForeignKey('utilisationfee.invoiceitem_id'), nullable = True)
    ucontext_id = Column(Integer, ForeignKey('utilisation_context.ucontext_id'), nullable = True)
    work_id = Column(Integer, ForeignKey('work.work_id'), nullable = True)
    society_id = Column(Integer, ForeignKey('collectingsociety.society_id'), nullable = True)

class UtilisationContext(Base):

    __tablename__ = 'utilisation_context'
    ucontext_id = Column(Integer,index = True, primary_key = True)