from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import jsonpickle

from cart.cartmanager import getCartManger


class ToOrder(View):
    def get(self, request):
        #获取参数
        cartitems = request.GET.get('cartitems', '')

        #判断用户是否登录
        if not request.session.get('user'):
            return render(request, 'login.html', {'cartitems':cartitems, 'redirect':'order'})
        #其他情况进入订单页面
        return HttpResponseRedirect('/order/order.html?cartitems='+cartitems)


class OrderList(View):
    def get(self, request):
        cartitems = request.GET.get('cartitems', '')
        print(cartitems)

        # 将json格式字符串转换成python对象（字典{goodsid:1,colorid:1,sizeid:1}）列表
        # [ {goodsid:1,colorid:1,sizeid:1},{goodsid:1,colorid:1,sizeid:1}]
        cartitemList = jsonpickle.loads("[" + cartitems + "]")

        # 将python对象列表转换成CartItem对象列表
        cartitemObjList = [getCartManger(request).get_cartitems(**item) for item in cartitemList if item]

        # 获取用户的默认收货地址
        address = request.session.get('user').address_set.get(isdefault=True)

        # 获取支付总金额
        totalPrice = 0
        for cm in cartitemObjList:
            totalPrice += cm.getTotalPrice()

        return render(request, 'order.html',
                      {'cartitemObjList': cartitemObjList, 'address': address, 'totalPrice': totalPrice})

