# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import ProcessedVideo 

class ProcessedVideoModelTestCase(TestCase):
    """Class Testing Model processed """

    def setUp(self):
        """
        Initial Test Settings
        """    

        self.processed_video = mommy.make(ProcessedVideo)

    def tearDown(self):
        """Final method"""
        self.processed_video.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        self.assertTrue('title' in dir(ProcessedVideo), 'Class Program does not have the field title')
        self.assertTrue('duration' in dir(ProcessedVideo), 'Class Program does not have the field start_time')
        self.assertTrue('name' in dir(ProcessedVideo), 'Class Program does not have the field end_time')


    def test_there_is_a_program(self):
        """test if you are creating a Program correctly"""

        self.assertEquals(ProcessedVideo.objects.count(), 1)
        self.assertEquals(ProcessedVideo.objects.all()[0].title, self.processed_video.title)
        self.assertEquals(ProcessedVideo.objects.all()[0].duration, self.processed_video.duration)
        self.assertEquals(ProcessedVideo.objects.all()[0].name, self.processed_video.name)
