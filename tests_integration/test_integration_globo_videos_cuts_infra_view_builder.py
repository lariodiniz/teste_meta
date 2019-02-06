#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import os


from codes.integration.globo_videos_cuts.infra.view import Builder
from tkinter import Frame, Label, Entry, Button, LEFT

class Qualquer:
    pass

class TestBuilderClass:
    """
    Tests the Builder class
    """

    def setup(self):
        """
        Initial Test Settings
        """    
        self.app = Qualquer()
        self.app._window = None


    def test_build(self):
        """        
        test if Builder create dicts
        """              

        Builder(self.app)

        assert 'labels' in dir(self.app)
        assert 'containers' in dir(self.app)
        assert 'entrys' in dir(self.app)
        assert 'button' in dir(self.app)

    def test_set_container(self):
        """        
        test if Builder create Frame
        """              

        b = Builder(self.app)
        b.Set_container("teste", 10, 5)

        assert "teste" in self.app.containers.keys()
        assert type(self.app.containers['teste']) is Frame 
        assert 10 == self.app.containers['teste']["pady"]
        assert 5 == self.app.containers['teste']["padx"]

    def test_set_font(self):
        """        
        test if Builder set fonts
        """              

        b = Builder(self.app)
        b.Set_font()

        assert self.app.font == ("Verdana", "8")
        assert self.app.font_title == ("Calibri", "9", "bold")   
        
    def test_set_entry(self):
        """        
        test if Builder create Entry
        """           

        b = Builder(self.app)
        b.Set_font()
        b.Set_container("teste", 10, 5)
        b.Set_entry("teste", 10, LEFT)

        assert "teste" in self.app.entrys.keys()
        assert type(self.app.entrys['teste']) is Entry
        assert 10 == self.app.entrys['teste']["width"]   
        assert  "Verdana 8" == self.app.entrys['teste']["font"]

    def test_set_label(self):
        """        
        test if Builder create Label
        """           

        b = Builder(self.app)
        b.Set_font()
        b.Set_container("teste", 10, 5)
        b.Set_label("teste", "Testando",LEFT)

        assert "teste" in self.app.labels.keys()
        assert type(self.app.labels['teste']) is Label        
        assert "Testando" == self.app.labels['teste']["text"]  
        assert  "Verdana 8" == self.app.labels['teste']["font"]


    def test_set_button(self):
        """        
        test if Builder create Button
        """           
        def testano():
            return "Função testano"   

        b = Builder(self.app)
        b.Set_font()
        b.Set_container("teste", 10, 5)
        b.Set_button("testanto", "testanto", 8, testano, LEFT, "teste")

        assert "testanto" in self.app.button.keys()
        assert type(self.app.button['testanto']) is Button
        assert "testanto" == self.app.button['testanto']["text"]
        assert  "Verdana 8" == self.app.button['testanto']["font"]
        assert 8 == self.app.button['testanto']["width"]        
        
