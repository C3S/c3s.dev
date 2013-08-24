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

class Accountant(User):

    Username = Column(String, ForeignKey('user.Username'),primary_key = True)
    __tablename__ = 'accountant'
    discriminator = Column(String)
    __mapper_args__ = {'polymorphic_on':discriminator}
    Rule = Column(String, ForeignKey('membershipfeecalculationrule.Rule'), nullable = True)