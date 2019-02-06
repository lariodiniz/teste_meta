#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from rest_framework import serializers
from core.models import ProcessedVideo


class ProcessedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedVideo
        fields = ('title', 'duration', 'name')
