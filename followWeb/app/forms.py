#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis

from flask_wtf import Form
from wtforms import BooleanField,TextField
from wtforms.validators import Required

 
class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
