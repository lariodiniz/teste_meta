# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Programs, CuttingJobs

class ProgramsViewTestCase(APITestCase):
    """Class Testing View Pogramas """

    def setUp(self):
        """
        Initial Test Settings
        """    

        self.url = reverse('api:programs')        
    
    def test_post_for_the_view_pogram(self):
        """verifies the return of the view program"""

        data = {'title':'teste', 'start_time':'00:00:00;FF', 'end_time':'01:02:03;FF', 'path':'pathteste'}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Programs.objects.count(), 1)
        self.assertEqual(Programs.objects.get().title, 'teste')    
        self.assertEqual(Programs.objects.get().start_time, '00:00:00;FF')    
        self.assertEqual(Programs.objects.get().end_time, '01:02:03;FF')    
        self.assertEqual(CuttingJobs.objects.get().pk, response.data['id_job'])    
        self.assertEqual('sussses', response.data['message'])
