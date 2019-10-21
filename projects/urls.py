from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.waiting_room, name='proof'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^tasks/(?P<task_id>\d+)/$', views.task, name='task'),
    #Страница для добавления новой темы
    url(r'^new_task/$', views.new_task, name='new_task'),
    #Страница для редактирования записи
    url(r'^edit_task/(?P<task_id>\d+)/$', views.edit_task, name='edit_task'),
    # Для добавления людей
    url(r'^add_emps/(?P<task_id>\d+)/$', views.add_emps, name='add_emps'),
    url(r'^rem_emps/(?P<emp_id>\d+)/(?P<task_id>\d+)/$', views.rem_emps, name='rem_emps'),
    url(r'^read_task/(?P<task_id>\d+)/$', views.read_task, name='read_task'),
    url(r'^results/$', views.search_task, name='search_task'),
    url(r'^make_leader/(?P<emp_id>\d+)/(?P<task_id>\d+)/$', views.make_leader, name='make_leader'),
]