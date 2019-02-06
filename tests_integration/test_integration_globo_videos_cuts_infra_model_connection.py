#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import os

from codes.integration.globo_videos_cuts.infra.model.connection import Connection

class TestConnectionClass:
    """
    Tests the Connection class
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

    def test_create_bd(self):
        """        
        test if bank is created
        """                
        
        assert os.path.exists(self.path+self.bd)

