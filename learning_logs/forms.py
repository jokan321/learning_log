1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : forms.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/12/31
6  # @Desc  :

from django import forms
from .models import Topic,Entry


#topic表单
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = {'text'}
        labels = {'text':''}

#entry表单
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'clos':80})}



