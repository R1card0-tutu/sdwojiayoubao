# -*- coding: utf-8 -*-
__author__ = 'michael'
__date__ = '2017/11/14 21:57'

from django.conf.urls import url, include
from .views import ProductListView, ProductDetailView

urlpatterns = [
    #
    url(r'^list/$', ProductListView.as_view(), name='product_list'),
    url(r'^detail/(?P<product_id>\d+)/$', ProductDetailView.as_view(), name='product_detail'),

]
