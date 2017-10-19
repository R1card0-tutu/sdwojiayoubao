# -*- coding: utf-8 -*-
__author__ = 'michael'
__date__ = '2017/10/19 21:20'
from django import forms
from captcha.fields import CaptchaField



class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


