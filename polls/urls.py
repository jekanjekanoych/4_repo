from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate-student/", views.student, name="generate-student"),
    path("generate-students/", views.students, name="generate-students/?count=100"),
]