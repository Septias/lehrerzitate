from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('new_teacher', views.TeacherCreate.as_view(), name='new_teacher')
]