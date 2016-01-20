# -*- coding:utf8 -*-

import wtforms
from wtforms_tornado import Form

"""
暂时还不会重写html代码，等以后在研究
"""


class LoginForm(Form):
    email = wtforms.StringField(u"Email Address", validators=[
        wtforms.validators.Email(),
        wtforms.validators.DataRequired(), ])
    password = wtforms.PasswordField(u"Password", validators=[
        wtforms.validators.DataRequired(),
    ])
