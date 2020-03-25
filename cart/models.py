from __future__ import unicode_literals

from django.db import models

# Create your models here.
from goods.models import *
from userapp.models import UserInfo


class CartItem(models.Model):
    goodsid = models.PositiveIntegerField()
    colorid = models.PositiveIntegerField()
    sizeid = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    isdelete = models.BooleanField(default=False)
    user = models.ForeignKey(UserInfo, on_delete=False)

    class Meta:
        #意思为在这个表中，每一行的user、artical字段必须唯一，否则报错。联合约束
        unique_together = ['goodsid','colorid','sizeid']

    def getGoods(self):
        return Goods.objects.get(id=self.goodsid)

    def getColor(self):
        return Color.objects.get(id=self.colorid)

    def getSize(self):
        return Size.objects.get(id=self.sizeid)


    def getTotalPrice(self):
        import math
        return math.ceil(float(self.getGoods().price)*int(self.count))