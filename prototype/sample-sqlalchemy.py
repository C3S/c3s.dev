# -*- coding: utf-8 -*-
##If you use Zope, you can get the session this way:

#from z3c.saconfig import named_scoped_session
#Session = named_scoped_session('default')
#session=Session()
#session.add(Person(name='Donald Duck')) #assume we have a Person class

##If you use the package standalone, do it that way:

from zope.configuration.xmlconfig import XMLConfig
import zope.component.event  #neccesary to initialize subscription system
import transaction
import c3s.dev
XMLConfig('configure.zcml',c3s.dev)()

#assume we have a few classes in a module 'personal'

from c3s.dev.creation import Agent, Work
from z3c.saconfig import named_scoped_session

Session = named_scoped_session('default')
session=Session()

#now play around with the database

agent=Agent(Username='schas')
work=Work(Name='bla')
work1=Work(Name='blorf')

work.children.append(work1)
session.add_all([agent,work])
#finally commit everything, now it lands in the db
transaction.commit()