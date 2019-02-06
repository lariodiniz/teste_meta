#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import ProcessedVideo
from core.serializer import ProcessedVideoSerializer


class GloboPlayView(APIView):
    """
    List all Programs
    """
    queryset = ProcessedVideo.objects.all()
    serializer_class = ProcessedVideoSerializer

    def post(self, request, format=None):
        serializer = ProcessedVideoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'message':'sussses'}, status=status.HTTP_201_CREATED)
            except:
                return Response('data sent invalid', status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

globo_play_view = GloboPlayView.as_view()