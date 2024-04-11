from django.http import HttpResponse
from django.shortcuts import render


def birth(request, y, m, d):
    html = "出生日期: {}年{}月{}日".format(y, m, d)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Django, how are you!")


def runoob(request):
    context = {}
    context["hello"] = "Hello World!"
    return render(request, "runoob.html", context)


def picture(request):
    return render(request, "index.html")


def p(request):
    html = 'This is a webpage, it has two pictures. <br/> <img src="/static/IMG_20231021_191505.jpg" width="112"height="150" alt=""/>'
    return HttpResponse(html)
