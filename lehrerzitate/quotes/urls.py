from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('new_teacher', views.TeacherCreate.as_view(), name='new_teacher'),
    path('report/<int:quote_id>', views.report, name="report"),
    path('ajax/get_likes', views.likes),
    path('ajax/like/<int:quote_id>', views.like),
    path('ajax/login', views.login, name='login')
]