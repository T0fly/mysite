from django.urls import path, re_path

from . import dbop, views

app_name = "polls"
urlpatterns = [
    path("", views.p),
    path("index/", views.index, name="index"),
    # re_path(r"^[A-Za-z]+$", views.get_page),
    # url参数传递
    path("page/<int:data>", views.getData),
    # path("<path:data>/", views.pathindex),
    # re_path("birth/<int:data>/", views.birth),
    re_path(r"^birthday/(?P<y>\d{1,4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})/$", views.birth),
    path("sv/", views.some_view),
    path("db/", views.db),
    path("dbc/", views.dbchange),
    path("qs/", views.query_stu),
    path("cno/<cno>", views.cno_010),
    path("student_list/", views.student_list),
    path("score_list/", views.score_list),
    path("aggr/", views.aggr),
    path("ann/", views.ann),
    path("rowsql/", views.rowsql),
    path("ceshi/", dbop.ceshi),
    path("oto/", views.oto),
    path("stc/", views.stc),
    path("sstc/", views.sstc),
]
