from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^get/$', views.next, name='next'),
    url(r'^new/user/$', views.new_user, name='new_user'),
]