from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from cart.cartmanager import *


class AddCart(View):
    def post(self, request):
        #获取当前操作的类型
        flag = request.POST.get('flag', '')
        #判断当前的类型
        if flag == 'add':
            #创建cartmanager对象
            cartManagerObj = getCartManger(request)
            #加入购物车操作
            cartManagerObj.add(**request.POST.dict())
        elif flag == 'plus':
            # 创建cartmanager对象
            cartManagerObj = getCartManger(request)
            #修改商品数量（添加商品数量操作）
            cartManagerObj.update(step=1, **request.POST.dict())
        elif flag == 'minus':
            # 创建cartmanager对象
            cartManagerObj = getCartManger(request)
            # 修改商品数量（减商品数量的操作）
            cartManagerObj.update(step=-1, **request.POST.dict())
        elif flag == 'delete':
            # 创建cartmanager对象
            cartManagerObj = getCartManger(request)
            # 逻辑移除商品（同步数据库）
            cartManagerObj.delete(**request.POST.dict())

        return HttpResponseRedirect('/cart/queryAll/')


class CartList(View):
    def get(self, request):
        # 创建cartmanager对象
        cartManagerObj = getCartManger(request)
        #查询所有购物项
        cartList = cartManagerObj.queryAll()
        return render(request, 'cart.html', {'cartList': cartList})