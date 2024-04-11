from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    return HttpResponse(
        "<h1>Django, how are you? <br> Welcome to the stumanager home page!</h1><h2>Menu</h2>"
        + "<a href='stu_show/'>学生信息</a>&nbsp&nbsp&nbsp&nbsp"
        + "<a href='class_show/'>班级信息</a>"
    )


def stu_show(request):
    return HttpResponse(
        "<h1>学生信息</h1>"
        + "<li><a href='/stm/stu_detail'>浏览学生</a></li><br>"
        + "<li><a href='/stm'>浏览学生班级</a></li><br>"
        + "<li><a href='/stm' style='color:blue'>返回主页</a></li>"
    )


from polls.models import scores, student


def stu_detail(request):
    html = "<h1>stu_detail</h1>" + "<h1>学生信息</h1>"
    students = student.objects.all()
    html += "学号    姓名    性别<br>"
    for i in students:
        html += f"{i.stuno} {i.name} {i.sex}<br>"
    html += "<a href='/stm/stu_show'>返回学生页面</a>"
    return HttpResponse(html)


def class_show(request):
    return HttpResponse(
        "<h1>班级信息</h1>"
        + "<li><a href='/stm/class_detail'>浏览班级信息</a></li><br>"
        + "<li><a href='/stm'>浏览班级学生信息</a></li><br>"
        + "<li><a href='/stm' style='color:blue'>返回主页</a></li>"
    )


def class_detail(request):
    html = "<h1>class_detail</h1>"
    score = scores.objects.all()
    html += "学号 课程号 成绩<br>"
    for i in score:
        html += f"{i.stuno} {i.cno} {i.grade}<br>"
    return HttpResponse(html)


def index(request):
    return render(request, "index.html", {"articles": 18})


def login(request):
    return HttpResponse("注册页面")


def book(request):
    return HttpResponse("读书页面")


def movie(request):
    return HttpResponse("电影页面")


def book_detail(request, book_id, catgray):
    text = "文章详情页,该文章ID是：%s，分类是：%s" % (book_id, catgray)
    return HttpResponse(text)
