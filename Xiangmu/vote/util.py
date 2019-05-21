from django.shortcuts import redirect,reverse
#调用流程
#将index函数作为fun实参传入checklogin，并且执行check（）

def checklogin(fun):
    def check(request,*args):
        #在cookie去用户
        # un=request.COOKIES.get('usernmae')

        #在session中取
        un=request.session.get('username')
        if un:
            return fun(request,*args)
        else:
            return redirect(reverse('vote:login'))
    return check