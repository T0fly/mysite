from django.urls import path

from . import views

app_name = "stumanager"
urlpatterns = [
    path("", views.home, name="home"),
    path("stu_show/", views.stu_show, name="stu_show"),
    path("class_show/", views.class_show, name="class_show"),
    path("stu_detail/", views.stu_detail, name="stu_detail"),
    path("class_detail/", views.class_detail, name="class_detail"),
]
