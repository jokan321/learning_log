1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : urls.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/12/31
6  # @Desc  :

from django.urls import path
from django.contrib.auth.views import LoginView
from .import views


urlpatterns = [
    #登録ページ
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #ログアウトページ
    path('logout',views.logout_view,name='logout'),
    #ユーザ新規登録
    path('register',views.register,name='register'),
]


