# -*- coding: utf-8 -*-

import xadmin
from xadmin import views

from .models import UsersProfile, EmailVerifyRecord, Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '我家有堡后台管理系统'
    site_footer = '山东我家有堡有限公司'
    menu_style = "accordion"


# class UsersProfileAdmin(object):
#     list_display = ['name', 'gender', 'mobile']
#     search_fields = ['name', 'gender', 'mobile']
#     list_filter = ['name', 'gender', 'mobile']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.register(UsersProfile, UsersProfileAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)