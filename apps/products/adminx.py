# -*- coding: utf-8 -*-
__author__ = 'michael'
__date__ = '2017/10/18 8:20'

import xadmin
from .models import Produce

class ProcuceAdmin(object):
    list_display = ['name', 'desc', 'detail', 'image', 'click_nums', 'add_time']
    search_files = ['name', 'desc', 'detail', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'image', 'click_nums', 'add_time']

xadmin.site.register(Produce, ProcuceAdmin)
