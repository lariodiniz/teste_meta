#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import os

from codes.integration.globo_videos_cuts.infra.model.connection import Connection
from codes.integration.globo_videos_cuts.infra.model import Config

class TestConfigClass:
    """
    Tests the Config class
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

    def config_config(self):
        c = Config(self.connection)
        c.path_text = 'teste_text'
        c.path_video = 'teste_video'        
        c.Insert()

        return c

    def clean_config(self, config):
        config.path_text = ''
        config.path_video = ''  

    def compare_config(self, config):
           
        assert config.path_text == 'teste_text'
        assert config.path_video == 'teste_video'        

    def test_insert(self):
        """        
        test if insert path
        """                
        config = self.config_config()

        self.clean_config(config)   

        config.Select()

        self.compare_config(config) 

    def test_upate(self):
        """        
        test if upate config
        """                
        config = self.config_config()

        config.path_text = 'teste_text 2'
        config.path_video = 'teste_video 2'
        config.version = '2'
        config.Update()

        self.clean_config(config)   

        config.Select()
        
        assert config.path_text == 'teste_text 2'
        assert config.path_video == 'teste_video 2'
        assert config.version == '2'

    def test_select(self):
        """        
        test if select config
        """                
        config = self.config_config()

        self.clean_config(config)   
        
        config.Select()

        self.compare_config(config) 

    def test_delete(self):
        """        
        test if delete config
        """                
        config = self.config_config()

        config.Delete()

        self.clean_config(config) 
        
        config.Select()
        
        assert config.path_text == ''
        assert config.path_video == ''
        assert config.version == ''      