#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

from sqlalchemy import Column, String,Integer,SmallInteger
from sqlalchemy.ext.declarative import declarative_base
 
ROLE_USER = 0
ROLE_ADMIN = 1


Base = declarative_base()


class User(Base):

    __tablename__ = 'user'


    id = Column(Integer, primary_key = True)
    nickname = Column(String(64), index = True, unique = True)
    email = Column(String(120), index = True, unique = True)
    role = Column(SmallInteger, default = ROLE_USER)
    
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.name)

