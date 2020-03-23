from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from userapp.models import *
from utils.code import gene_code
from django.core.serializers import serialize

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self,request):
        #获取参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        #插入数据库
        user = UserInfo.objects.create(uname=uname,pwd=pwd)
        if user:
            #将用户信息存入session
            request.session['user'] = user
            return HttpResponseRedirect('/user/center/')

        return HttpResponseRedirect('/user/register/')


class CheckUname(View):
    def get(self, request):
        #获取参数
        uname = request.GET.get('uname', '')
        #根据用户名查询数据库
        userList = UserInfo.objects.filter(uname=uname)
        flag = False
        #判断userList是否为空
        if userList:
            flag = True
        return JsonResponse({'flag': flag})

#用户中心
class Center(View):
    def get(self, request):
        return render(request, 'center.html')

#退出功能
class Logout(View):
    def post(self, request):
        if 'user' in request.session:
            #删除user
            del request.session['user']
        return JsonResponse({'delflag': True})


class Login(View):
    def get(self,request):
        return render(request, "login.html")
    def post(self, request):
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')

        #查询数据库
        userList = UserInfo.objects.filter(uname=uname, pwd=pwd )
        if userList:
            #把用户名存入session中
            request.session['user']=userList[0]
            #成功后到用户中心
            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/login/')



class LoadCode(View):
    def get(self, request):
        img, str = gene_code()
        print('str==='+str)

        #将生成的验证码存放至session中
        request.session['sessionCode'] = str

        return HttpResponse(img, content_type='image/png')


class Checkcode(View):
    def get(self, request):
        #获取验证码
        code = request.GET.get('code', '')
        #获取session中的字符
        sessionCode = request.session.get('sessionCode')
        #判断code和sessionCode是否相等
        flag = code == sessionCode
        return JsonResponse({'checkFlag': flag})


class Addressa(View):
    def get(self, request):
        user = request.session.get('user', '')
        # 获取当前登录用户的所有收货地址
        addrList = user.address_set.all()

        return render(request, 'address.html', {'addrList': addrList})

    def post(self, request):
        #获取信息
        aname = request.POST.get('aname', '')
        aphone = request.POST.get('aphone', '')
        addr = request.POST.get('addr', '')
        #从session中获取user
        user = request.session.get('user')
        #插入数据库
        address = Address.objects.create(aname=aname, aphone=aphone, addr=addr, userinfo=user, isdefault=(lambda count: True if count == 0 else False)(user.address_set.all().count()))
        #获取当前用户的所有地址
        addrList = user.address_set.all()
        #在页面中显示
        return render(request, 'address.html', {'addressList': addrList})



# class LoadArea(View):
#     def get(self, request):
#         pid = request.GET.get('pid', -1)
#         pid = int(pid)
#         #通过pid查询区划信息
#         areaList = Area.objects.filter(parentid=pid)
#         #序列化areaList为子符串
#         jareaList = serialize('json', areaList)
#         return JsonResponse({'jareaList': jareaList})

