from django.http import HttpResponse
from django.shortcuts import render


def birth(request, y, m, d):
    html = "出生日期: {}年{}月{}日".format(y, m, d)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("这是我的网页")


def runoob(request):
    context = {}
    context["hello"] = "Hello World!"
    return render(request, "runoob.html", context)


def picture(request):
    return render(request, "index.html")
