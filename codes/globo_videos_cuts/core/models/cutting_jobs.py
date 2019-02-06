# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

from core.models import Programs

class CuttingJobs(models.Model):

    STATUS_MODE = (
        (0, 'process'),
        (1, 'success'),
        (2, 'failure'),        
    )

    status = models.IntegerField('status', choices=STATUS_MODE, default=0, blank=True)    
    program = models.ForeignKey(Programs, verbose_name='program', on_delete=models.CASCADE)
    path = models.CharField('path', max_length=200)

    class Meta:
        verbose_name = 'Cutting Job'
        verbose_name_plural = 'Cutting Jobs' 
