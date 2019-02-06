#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from .views import programs_view, cutting_job_view, globo_play_view


app_name = 'core'

urlpatterns = format_suffix_patterns([
    path('programs/', programs_view, name='programs'),        
    path('cutting_jobs/<int:pk>/', cutting_job_view, name='cutting_jobs'), 
    path('globo_play/', globo_play_view, name='globo_play'), 
        
])
