from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^register/$', core_views.register, name='register'),
]