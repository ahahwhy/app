from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("start/", views.start, name="start"),
    path("discover/", views.discover, name="discover"),
    path("about/", views.about, name="about"),
    path("project/", views.project, name="project"),
]
