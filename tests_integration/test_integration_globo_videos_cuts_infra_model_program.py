#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import os

from codes.integration.globo_videos_cuts.infra.model.connection import Connection
from codes.integration.globo_videos_cuts.infra.model import Pograms

class TestPogramsClass:
    """
    Tests the Pograms class
    """

    def setup(self):
        """
        Initial Test Settings
        """    
        self.path ='tests_integration\\'
        self.bd = 'teste.db'

        self.connection = Connection(self.path,self.bd)
        
    def tearDown(self):
        if os.path.exists(self.path+self.bd):
            os.remove(self.path+self.bd)
           
    def config_pograms(self):
        p = Pograms(self.connection) 
        p.id = 1          
        p.start_time = '00:00:54;16'
        p.end_time = '00:51:00;00'
        p.title = 'teste'
        p.duration = '00:50:6;00'
        p.reconile_key = 1
        p.Insert()

        return p

    def clean_pograms(self, program):
        program.start_time = ''
        program.end_time = ''
        program.title = ''
        program.duration = ''
        program.reconile_key = 0

    def compare_pograms(self, program):
        
        assert program.start_time == '00:00:54;16'
        assert program.end_time == '00:51:00;00'
        assert program.title == 'teste'
        assert program.duration == '00:50:6;00'
        assert program.reconile_key == 1

    def test_insert(self):
        """        
        test if insert files
        """     
        program = self.config_pograms()
        self.clean_pograms(program)
        program.Select(1)
        self.compare_pograms(program)
        
    def test_upate(self):
        """        
        test if upate config
        """     

        program = self.config_pograms()

        program.title = "teste 2"
        program.reconile_key = 4 
        program.Update()

        self.clean_pograms(program)

        program.Select(1)
        
        assert program.title == "teste 2"
        assert program.reconile_key == 4 
        

    def test_select(self):
        """        
        test if select config
        """                
        program = self.config_pograms()
        self.clean_pograms(program)
        
        program.Select(1)
        print(program.start_time)

        self.compare_pograms(program)

    def test_delete(self):
        """        
        test if delete config
        """                
        program = self.config_pograms()

        program.Delete()
        
        program.Select(1)
        
        assert program.title == ""      