from django.urls import path
from . import views


app_name = 'explorer'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('new', views.question_create, name='question_new'),
    path('title/<str:title>', views.question_detail, name='question_detail')

]