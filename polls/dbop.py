import pymysql
from django.db.models import Avg, Q, Subquery
from django.db.models.expressions import RawSQL
from django.db.models.functions import Left
from django.http import HttpResponse

from polls.models import scores, student


def ceshi(request):
    # 查询数据
    # ds = Student.objects.values("stu_name", "stu_gender")
    # html = ""
    # for a in ds:
    #     html = html + "%s %s\n" % (a["stu_name"], a["stu_gender"])
    #     return HttpResponse(html)

    # 查询集操作
    ds = student.objects.filter(name__startswith="王")
    html = ""
    if ds:
        for a in ds:
            html = html + "%s %s\n<br>" % (a.stuno, a.name)
    else:
        html = "查无此人"
    return HttpResponse(html)

    # 查询集操作
    # ds=Student.objects.filter(stu_name__startswith="李")
    # html=""
    # if ds:
    #     for a in ds:
    #         html = "%s %s\n" % (a.stu_id, a.stu_name)
    # else:
    #     html="查无此人"
    # return HttpResponse(html)

    # 聚合函数aggregate使用
    # ds = Scores.objects.aggregate(Avg("grade"), Max("grade"))
    # html = "平均值：%s,\t 最大值：%s\n" % (ds['grade__avg'],ds['grade__max'])
    # return HttpResponse(html)

    # 聚合函数aggregate查询某门课程的平均值和最高分
    ds = Scores.objects.filter(cno="010").aggregate(Avg("grade"), Max("grade"))
    html = "平均值：%s,\t 最大值：%s\n" % (ds["grade__avg"], ds["grade__max"])
    return HttpResponse(html)

    # annotate使用
    ds = Scores.objects.values("cno").annotate(Avg("grade"), Max("grade"))
    html = "课程号  平均成绩  最高分<br>"
    for a in ds:
        html = (
            html
            + a["cno"]
            + "\t\t"
            + str(a["grade__avg"])
            + "\t\t"
            + str(a["grade__max"])
            + "<br>"
        )
    return HttpResponse(html)

    # 数据库函数表达式
    ds = Student.objects.annotate(first_name=Left("name", 1))
    for i in range(len(ds)):
        html = (
            html
            + "学生姓氏：%s,\t 姓名：%s\n" % (ds[i].first_name, ds[i].name)
            + "<br>"
        )
    return HttpResponse(html)

    # 原始SQL表达式
    ds = Scores.objects.all().annotate(
        grade90=RawSQL("select count(*)from Scores where grade>=%s", (90,))
    )
    html = ""
    for a in ds.order_by("-grade")[:3]:
        html = html + "<br>编号：%s,学号：%s,成绩：%d\n" % (a.id, a.stuno, a.grade)
    return HttpResponse(html)

    # 执行简单查询
    # ds = Scores.objects.raw("select * from Scores where grade>=80")
    ds = Scores.objects.raw("select * from app01_scores where cno=%s", ["20"])
    ds = scores.objects.raw(
        "select * from scores where cno=%s and grade>=%s ", ["020", 90]
    )

    html = ""
    for a in ds:
        html = html + "<br>编号：%s,\t\t学号：%s,\t\t课程号：%s,\t\t成绩：%d" % (
            a.id,
            a.stuno,
            a.cno,
            a.grade,
        )
    return HttpResponse(html)

    # raw执行insert update delete
    ds = Scores.objects.raw(
        "insert into Scores(id,stuno,cno,grade) values('11','0006','010','90')"
    )
    ds = Scores.objects.raw("update Scores set grade=%s where id=11", [100])
    ds = Scores.objects.raw("delete from Scores where id=11")
    ds.query._execute_query()  # 立即执行查询命令
    ds = Scores.objects.raw("select * from Scores")
    html = ""
    for a in ds:
        html = html + "<br>编号：%s,课程号：%s,学号：%s,成绩：%d" % (
            a.id,
            a.stuno,
            a.cno,
            a.grade,
        )
    return HttpResponse(html)

    # 直接执行SQL语句
    conn = pymysql.connect(
        host="127.0.0.1", port=3306, user="root", passwd="3312944", db="mysite"
    )
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    # cursor.execute("select * from Scores")
    cursor.execute("select * from Scores where cno=%s", ["020"])
    # html = cursor.fetchall()
    html = ""
    for a in cursor.fetchall():  # 所有记录
        html = html + "<br>编号：%s,课程号：%s,学号：%s,成绩：%d" % (
            a[0],
            a[1],
            a[2],
            a[3],
        )
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return HttpResponse(html)

    # 直接执行insert update delete语句
    conn = pymysql.connect(
        host="127.0.0.1", port=3306, user="root", passwd="3312944", db="mysite"
    )
    cursor = conn.cursor()
    # cursor.execute("insert into mysite.Scores(id,stuno,cno,grade) values('13','0007','020',100)")
    cursor.execute("update Scores set grade=100 where id=13")
    cursor.execute("delete from Scores where id=11")
    cursor.execute("select * from mysite.Scores")
    conn.commit()
    html = cursor.fetchall()
    for a in cursor.fetchall():  # 所有记录
        html = html + "<br>编号：%s,课程号：%s,学号：%s,成绩：%d" % (
            a[0],
            a[1],
            a[2],
            a[3],
        )
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return HttpResponse(html)
