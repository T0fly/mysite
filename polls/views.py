# Create your views here.
from glob import escape

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from polls.models import s


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_page(request):
    return HttpResponse("get_page,字母")
    # return render(request, "index.html")
    # return HttpResponse("这是polls下的pic方法的return")


def pic(request):
    return HttpResponse("欢迎学习Django框架")


def p(request):
    return render(request, "index.html")


def getData(request, data):
    html = "第%d个页,类型为%s" % (data, type(data))
    return HttpResponse(html)


def pathindex(request, data):
    return HttpResponse(escape(data))


def birth(request, y, m, d):
    html = "出生日期: {}年{}月{}日".format(y, m, d)
    return HttpResponse(html)


def some_view(request):
    # 使用命名空间和 URL 名称来生成 URL
    url = reverse("polls:index")  # 'polls' 是应用程序的命名空间，'index' 是 URL 名称
    return HttpResponseRedirect(url)


def dbchange(request):
    # # 查询单个记录
    # students = s.objects.get(stuno="001")
    stu = s.objects.get(stuno="001")
    if stu.stuname == "李四":
        stu.stuname = "张三"
    else:
        stu.stuname = "李四"
    stu.save()
    stu = s.objects.values_list(
        "stuno", "stuname", "stuclass", "stuage", "stusex", "stuphone", "stuaddress"
    )
    html = ""
    for i in stu:
        for j in range(0, 7):
            html = html + i[j] + " "
    return HttpResponse(html)


def db(request):
    # # 查询所有记录
    # students = s.objects.all()
    # 查询满足条件的记录
    students = s.objects.filter(stuname="张三")

    stu = s.objects.values_list(
        "stuno", "stuname", "stuclass", "stuage", "stusex", "stuphone", "stuaddress"
    )
    html = ""
    # student = s.objects.all()
    for i in stu:
        # html = html + i.stuno + " " + i.stuname + " " + i.stuclass + "</br>"
        for j in range(0, 7):
            html = html + i[j] + " "
    return HttpResponse(html)


from polls.models import scores, student


def query_stu(request):
    st = student
    st = student.objects.filter(sex="女", name__contains="王")
    html = ""
    for i in st:
        html += i.stuno + " " + i.name + " " + i.sex + " " + str(i.birthdate) + "<br>"
    return HttpResponse(html)


def cno_010(request, cno):
    stu_count = scores.objects.filter(cno=cno).distinct().count()
    stu_no = scores.objects.filter(cno=cno).values_list("stuno", flat=True)
    # 设置flat=True参数把二维结构扁平化成一维列表
    stu_names = student.objects.filter(stuno__in=stu_no).values_list("name", flat=True)
    html = f"选修{cno}课程的学生人数:{stu_count}<br>"
    html += "学生姓名:<br>"
    for name, stuno in zip(stu_names, stu_no):
        html += f"{stuno} {name}<br>"
    return HttpResponse(html)


def student_list(request):
    students = student.objects.all()
    html = "学号    姓名    性别<br>"
    for i in students:
        html += f"{i.stuno} {i.name} {i.sex}<br>"
    return HttpResponse(html)


def score_list(request):
    score = scores.objects.all()
    html = "学号 课程号 成绩<br>"
    for i in score:
        html += f"{i.stuno} {i.cno} {i.grade}<br>"
    return HttpResponse(html)
