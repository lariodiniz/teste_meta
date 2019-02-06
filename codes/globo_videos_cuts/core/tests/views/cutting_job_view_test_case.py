# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from model_mommy import mommy


from core.models import Programs, CuttingJobs

class CuttingJobsViewTestCase(APITestCase):
    """Class Testing View Pogramas """

    def setUp(self):
        """
        Initial Test Settings
        """    
        self.programs = mommy.make(Programs)
        self.jobs = mommy.make(CuttingJobs, program = self.programs)
        self.url = reverse('api:cutting_jobs', kwargs={'pk':self.jobs.pk}) 
          

    def tearDown(self):
        """Final method"""
        self.jobs.delete()
        self.programs.delete()

    def test_get_for_the_view_cutting_jobs(self):
        """verifies the return of the view program"""

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('success', response.data['message'])

        """ self.jobs.status = 1
        self.jobs.save()

        response = self.client.get(self.url)

        self.assertEqual('success', response.data['message'])"""
