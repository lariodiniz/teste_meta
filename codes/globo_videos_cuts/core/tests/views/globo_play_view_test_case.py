# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import ProcessedVideo


class GloboPlayViewTestCase(APITestCase):
    """Class Testing View Pogramas """

    def setUp(self):
        """
        Initial Test Settings
        """    

        self.url = reverse('api:globo_play')        
    
    def test_post_for_the_view_pogram(self):
        """verifies the return of the view program"""

        data = {'title':'teste', 'duration':'10:15:00;FF', 'name':'teste name'}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('sussses', response.data['message'])
        self.assertEquals(ProcessedVideo.objects.count(), 1)
        self.assertEquals(ProcessedVideo.objects.all()[0].title, 'teste')
        self.assertEquals(ProcessedVideo.objects.all()[0].duration, '10:15:00;FF')
        self.assertEquals(ProcessedVideo.objects.all()[0].name, 'teste name')        

