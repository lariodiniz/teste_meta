# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import Programs

class ProgramsModelTestCase(TestCase):
    """Class Testing Model Pogramas """

    def setUp(self):
        """
        Initial Test Settings
        """    

        self.program = mommy.make(Programs)

    def tearDown(self):
        """Final method"""
        self.program.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        self.assertTrue('title' in dir(Programs), 'Class Program does not have the field title')
        self.assertTrue('start_time' in dir(Programs), 'Class Program does not have the field start_time')
        self.assertTrue('end_time' in dir(Programs), 'Class Program does not have the field end_time')


    def test_there_is_a_program(self):
        """test if you are creating a Program correctly"""

        self.assertEquals(Programs.objects.count(), 1)
        self.assertEquals(Programs.objects.all()[0].title, self.program.title)
        self.assertEquals(Programs.objects.all()[0].start_time, self.program.start_time)
        self.assertEquals(Programs.objects.all()[0].end_time, self.program.end_time)
