# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Produce(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"产品名")
    desc = models.CharField(max_length=300, verbose_name=u"产品简介")
    detail = models.TextField(verbose_name=u"产品详情")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"产品图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"产品"
        verbose_name_plural = verbose_name


