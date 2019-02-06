# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

class ProcessedVideo(models.Model):

    title = models.CharField('title', max_length=200)
    name = models.CharField('name', max_length=200)
    duration = models.CharField('duration', max_length=12)

    
    class Meta:
        verbose_name = 'Processed Video'
        verbose_name_plural = 'Processed Videos' 