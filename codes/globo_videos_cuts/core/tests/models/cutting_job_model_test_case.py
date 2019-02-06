# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import CuttingJobs, Programs

class CuttingJobsModelTestCase(TestCase):
    """Class Testing Model Pogramas """

    def setUp(self):
        """
        Initial CuttingJobs Settings
        """    
        self.programs = mommy.make(Programs)
        self.jobs = mommy.make(CuttingJobs, program = self.programs)

    def tearDown(self):
        """Final method"""
        self.jobs.delete()
        self.programs.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        self.assertTrue('status' in dir(CuttingJobs), 'Class CuttingJobs does not have the field status')
        self.assertTrue('program' in dir(CuttingJobs), 'Class CuttingJobs does not have the field program')
        self.assertTrue('path' in dir(CuttingJobs), 'Class CuttingJobs does not have the field path')
        

    def test_there_is_a_job(self):
        """test if you are creating a CuttingJobs correctly"""

        self.assertEquals(CuttingJobs.objects.count(), 1)
        self.assertEquals(CuttingJobs.objects.all()[0].status, self.jobs.status)
        self.assertEquals(CuttingJobs.objects.all()[0].program, self.jobs.program)
        self.assertEquals(CuttingJobs.objects.all()[0].path, self.jobs.path)        
        self.assertEquals(CuttingJobs.objects.all()[0].program, self.programs)
