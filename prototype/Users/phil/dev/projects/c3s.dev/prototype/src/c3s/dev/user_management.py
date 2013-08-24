# -*- coding: utf-8 -*-
from c3s.dev.saconfig import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)

class User(Base):

    __tablename__ = 'user'
    discriminator = Column(String)
    __mapper_args__ = {'polymorphic_on':discriminator}
    Username = Column(String,index = True, primary_key = True)