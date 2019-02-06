# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

class Programs(models.Model):

    title = models.CharField('title', max_length=200)
    start_time = models.CharField('start time', max_length=12)
    end_time = models.CharField('end time', max_length=12)

    
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs' 
