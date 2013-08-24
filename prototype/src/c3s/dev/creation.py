# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from c3s.dev.user_management import User
from c3s.dev.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class Member(User):

    Username = Column(String, ForeignKey('user.Username'),primary_key = True)
    __tablename__ = 'member'
    discriminator = Column(String)
    __mapper_args__ = {'polymorphic_on':discriminator}
    Name = Column(String)
    Address = Column(String)
    Shares = Column(String)
    invoicereceiver_id = Column(Integer, ForeignKey('invoicereceiver.invoicereceiver_id'), nullable = True)

class Agent(User):

    __mapper_args__ = {'polymorphic_identity':'agent'}
    Username = Column(String, ForeignKey('user.Username'),primary_key = True)
    __tablename__ = 'agent'
    Address = Column(String)
    Name = Column(String)
    artist_Username = Column(String, ForeignKey('member.Username'), nullable = True)
    invoicereceiver_id = Column(Integer, ForeignKey('invoicereceiver.invoicereceiver_id'), nullable = True)

class Work(Base):

    __tablename__ = 'work'
    Name = Column(String)
    Licence = Column(String)
    Acoustic_fingerprint = Column(String)
    work_id = Column(Integer,index = True, primary_key = True)
    Username = Column(String, ForeignKey('creator.Username'), nullable = True)
    children = association_proxy("children_assocs", "work", 
                                creator=lambda c: WorkParent(children=c))
    parents = association_proxy("parents_assocs", "work", 
                                creator=lambda c: WorkParent(parents=c))
    children_assocs = relationship('WorkParent', backref = 'parents', primaryjoin = 'WorkParent.parents_work_id == Work.work_id')
    parents_assocs = relationship('WorkParent', backref = 'children', primaryjoin = 'WorkParent.children_work_id == Work.work_id')

class Creator(Member):

    __mapper_args__ = {'polymorphic_identity':'creator'}
    Username = Column(String, ForeignKey('member.Username'),primary_key = True)
    __tablename__ = 'creator'

class WorkParent(Base):

    __tablename__ = 'workparent'
    children_work_id = Column(Integer, ForeignKey('work.work_id'), primary_key = True, nullable = False)
    parents_work_id = Column(Integer, ForeignKey('work.work_id'), primary_key = True, nullable = False)