from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
def home(request):
    return HttpResponse(
        "<h1>Django, how are you? </h1><h2>Welcome to the Student Manage system home page!<br>Menu</h2>"
        + "<a href='"
        + reverse("stumanager:stu_show")
        + "'>学生信息</a>&nbsp&nbsp&nbsp&nbsp"
        + "<a href='class_show/'>班级信息</a>"
    )


def stu_show(request):
    # 使用 reverse() 函数生成名为 'stu_show' 的 URL
    show_student_url = reverse("stumanager:show_student")
    # 这里的 stumanager 是你在 urls.py 文件中指定的应用程序命名空间。
    # 在 HTML 中嵌入动态生成的链接
    html = (
        "<h1>学生信息</h1>"
        + f"<li><a href='{show_student_url}' style='color:green'>浏览学生</a></li><br>"
        + "<li><a href='/stm/show_class_of_student'>浏览学生班级</a></li><br>"
        + "<li><a href='/stm' style='color:blue'>返回主页</a></li>"
    )
    return HttpResponse(html)


def class_show(request):
    return HttpResponse(
        "<h1>班级信息</h1>"
        + "<li><a href='/stm/show_class'>浏览班级信息</a></li><br>"
        + "<li><a href='/stm/show_student_of_class'>浏览班级学生信息</a></li><br>"
        + "<li><a href='/stm' style='color:blue'>返回主页</a></li>"
    )


from stumanage.models import Class, Student


# 一对多关系
def addclass(request):
    Class1 = Class(class_name="软件1211")
    Class1.save()
    student1 = Student(student_name="张三", Class=Class1)
    student1.save()

    Class2 = Class(class_name="软件1212")
    Class2.save()
    student2 = Student(student_name="李四", Class=Class2)
    student2.save()

    Class3 = Class(class_name="软件1213")
    Class3.save()
    student3 = Student(student_name="王五", Class=Class3)
    student3.save()

    return HttpResponse("添加班级成功")


def show_student(request):
    students = Student.objects.all()
    html = "<h1>学生信息</h1>学号 姓名<br>"
    for student in students:
        html += f"{student.id} {student.student_name} <br>"
    html += "<a href='/stm/stu_show'>返回学生页面</a>"
    return HttpResponse(html)


def show_class_of_student(request):
    students = Student.objects.all()
    html = "<h1>学生信息</h1>学号 姓名 班级号 班级名<br>"
    for student in students:
        html += f"{student.id} {student.student_name} {student.Class.id} {student.Class.class_name}<br>"
    html += "<a href='/stm/stu_show'>返回学生页面</a>"
    return HttpResponse(html)


def show_class(request):
    classes = Class.objects.all()
    html = "<h1>班级信息</h1>班级号 班级名<br>"
    for c in classes:
        html += f"{c.id} {c.class_name} <br>"
    html += "<a href='/stm/class_show'>返回班级页面</a>"
    return HttpResponse(html)


def show_student_of_class(request):
    classes = Class.objects.all()
    html = "<h1>班级学生</h1>班级号 班级名 学号 姓名<br>"
    for c in classes:
        for student in c.student_set.all():
            html += f"{c.id} {c.class_name} {student.id} {student.student_name}<br>"
    html += "<a href='/stm/class_show'>返回班级页面</a>"
    return HttpResponse(html)
