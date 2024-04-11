from django.urls import path

from . import views

app_name = "stumanager"
urlpatterns = [
    path("", views.home, name="home"),
    path("stu_show/", views.stu_show, name="stu_show"),
    path("class_show/", views.class_show, name="class_show"),
    path("show_student/", views.show_student, name="show_student"),
    path(
        "show_class_of_student/",
        views.show_class_of_student,
        name="show_class_of_student",
    ),
    path("show_class/", views.show_class, name="show_class"),
    path(
        "show_student_of_class/",
        views.show_student_of_class,
        name="show_student_of_class",
    ),
    path("addclass/", views.addclass),
]
