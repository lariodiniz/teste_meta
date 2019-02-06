#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import os

from codes.integration.globo_videos_cuts.infra.model.connection import Connection
from codes.integration.globo_videos_cuts.infra.model import Files

class TestFilesClass:
    """
    Tests the Files class
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
            
    def config_file(self):
        files = Files(self.connection)           
        files.id = 1
        files.name = "teste"
        files.line = 15 
        files.Insert()

        return files

    def test_select(self):
        """        
        test if select config
        """                
        files = self.config_file()

        files.name = ""
        
        files.Select(1)        

        assert files.name == 'teste'

    def test_insert(self):
        """        
        test if insert files
        """     

        files = self.config_file()

        files.name = ""
        files.line = 0  

        files.Select(1)
        
        assert files.id == 11
        assert files.name == "teste"
        assert files.line == 15

    def test_upate(self):
        """        
        test if upate config
        """     

        files = self.config_file()


        files.name = "teste 2"
        files.line = 1 
        files.Update()


        files.id = 0
        files.name = ""
        files.line = 0  

        files.Select(1)        

        assert files.id == 1
        assert files.name == "teste 2"
        assert files.line == 1

    def test_delete(self):
        """        
        test if delete config
        """                
        files = self.config_file()

        files.Delete()
        
        files.Select(1)
        
        assert files.name == ""      