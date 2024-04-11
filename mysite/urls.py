"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(r"^birthday/(?P<y>\d{1,4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})/$", views.birth),
    path("", views.hello, name="hello"),
    path("polls/", include("polls.urls")),
    path("stm/", include("stumanage.urls")),
    path("admin/", admin.site.urls),
    path("hello/", views.hello, name="hello"),
    path("runoob/", views.runoob),
    path("pic/", views.picture),
    path("rp/", views.p),
]
