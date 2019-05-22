from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import question,choice,MyUser
from  django.views.generic import View
# Create your views here.







# class login(View):
#     def get(self,request):
#         return render(request,'vote/login.html',locals())
#     def post(self,request):
#         username=request.POST.get('username')
#         if username=='abc':
#             #denglucg需要将用户相关储存
#             res=redirect(reverse('vote:index'))
#             res.set_cookie('username',username)
#             return res
#         else:
#
#             return render(request,'vote/login.html',{'error':'用户名错误'})

def login(request):
    if request.method=='GET':
        return render(request,'vote/login.html')
    else:
        username = request.POST.get('username')
        if username =='abc':
            # denglucg需要将用户相关储存
            res = redirect(reverse('vote:index'))
            #设置cookie 完成登录
            # res.set_cookie('username', username)

            #通过scssion完成的那个路
            request.session['username']=username
            return res
        else:

            return render(request, 'vote/login.html', {'error': '用户名错误'})

def logout(request):
    res=redirect(reverse('vote:login'))
    request.session.flush()
    return res

def regist(request):
    if request.method=='POST':
        username=request.POST.get('username_regi')
        pwd=request.POST.get('password_regi')
        pwd2=request.POST.get('password_regi_2')
        print(username,pwd2,pwd)
        error=None
        if pwd !=pwd2:
            error='密码不一致'

            return render(request,'vote/login.html',{'error':error})
        else:
            MyUser.objects.create_user(username=username,password=pwd,url='http://baidu.com')
            return redirect(reverse('vote:login'))



def index(request):
    if request.method=='POST':
        username=request.POST.get('')
    # return HttpResponse('首页')
    un=request.session.get('username')
    if un:
        username=un
        q = question.objects.all()
        return render(request,'vote/index.html',locals())
    else:
        return redirect(reverse('vote:login'))


def checklogin(fun):
    def check(request):
        un=request.COOKIES.get('usernmae')
        if un:
            username=un
            fun(request)
        else:
            return redirect(reverse('vote:login'))
        return check

def detail(request,id):
    # return HttpResponse('detail')
    q = question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'vote/detail.html',{'q':q})
    elif request.method == 'POST':
        c_txet=request.POST['choice']
        # choice.objects.incresevotes(c_txet)
        a=choice.objects.get(pk=c_txet)
        a.votes+=1
        a.save()

        # return HttpResponse('投票成功')
        return HttpResponseRedirect('/vote/result/%s/' % (id,))

def result(request,id):
    # return HttpResponse('result')
    q=question.objects.get(pk=id)
    return render(request,'vote/result.html',locals())


