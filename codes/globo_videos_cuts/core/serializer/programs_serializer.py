#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from rest_framework import serializers
from core.models import Programs


class ProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = ('title', 'start_time', 'end_time')
