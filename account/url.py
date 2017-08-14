from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url, include
from account import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userlist/$',views.user_list, name='userlist'),
    url(r'^userdel/$', views.userdel, name='userdel'),
    url(r'^userupdate_msg/$',views.userupdate_msg,name='userupdate_msg'),
    url(r'^update_sure/$',views.update_sure,name='update_sure'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^updatepwd_sure/$', views.updatepwd_sure, name='updatepwd_sure'),

]