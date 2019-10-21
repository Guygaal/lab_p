from django.conf.urls import url
from django.contrib.auth.views import LoginView
from .views import logout_view
from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    #Страница регистрации
    url(r'^register/$', views.register, name='register'),
]
