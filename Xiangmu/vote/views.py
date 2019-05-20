from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import question,choice
# Create your views here.

def index(request):
    # return HttpResponse('首页')
    q = question.objects.all()

    return render(request,'vote/index.html',{'q':q})

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


