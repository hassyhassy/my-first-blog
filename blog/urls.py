# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:37:20 2022

@author: kouki
"""

from django.urls import path
from . import views

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
]