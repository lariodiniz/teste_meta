#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from core.models import CuttingJobs


class CuttingJobsView(APIView):
    """
    List one CuttingJobs.
    """
    queryset = CuttingJobs.objects.all()
    

    def get_object(self, pk):
        try:
            return CuttingJobs.objects.get(pk=pk)
        except CuttingJobs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        job.status = 1
        job.save()
        return Response({'id_job':job.pk, 'message':job.get_status_display()}, status=status.HTTP_200_OK)

cutting_job_view = CuttingJobsView.as_view()