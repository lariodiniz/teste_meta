#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Programs, CuttingJobs
from core.serializer import ProgramsSerializer

class ProgramsView(APIView):
    """
    List all Programs, or create a new Program.
    """
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer

    def post(self, request, format=None):

        if ('path' not in request.data.keys()):
           return Response('data sent invalid', status=status.HTTP_400_BAD_REQUEST)

        path = request.data['path']
        del request.data['path']

        serializer = ProgramsSerializer(data=request.data)
        if serializer.is_valid():
            program = serializer.save()
            job = CuttingJobs()
            job.program = program
            job.path = path
            job.save()
            try:
                return Response({'id_job':job.pk, 'message':'sussses'}, status=status.HTTP_201_CREATED)
            except:
                return Response('data sent invalid', status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

programs_view = ProgramsView.as_view()