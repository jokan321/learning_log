#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: JO_KAAN
# @Date  : 2019/12/29
# @Desc  :



from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('topics',views.topics,name='topics'),
    path('topic/(?p<topic_id>\+d)/$',views.topic,name='topic'),
    path('new_topic',views.new_topic,name='new_topic'),
    path('new_entry/(?p<topic_id>\+d)/$',views.new_entry,name='new_entry'),
    path('edit_entry/(?p<entry_id>+d)/$',views.edit_entry,name='edit_entry'),
]
