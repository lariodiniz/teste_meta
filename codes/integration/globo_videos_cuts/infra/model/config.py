#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from .connection import Connection
from .model_base import ModelBase


class Config(ModelBase):
    """
    Config model class
    """
  
    def __init__(self, connection = None, **kwargs):
        super(Config, self).__init__(connection,**kwargs)
        

    def _clear(self):
        """Clear the fields"""
        self.version = ""
        self.path_video = ""
        self.path_text = ""
  
  
    def Insert(self):
        """Insert in the bd"""
        if self._execute("""insert into config 
                        ( version, path_video, path_text ) 
                        values 
                        ('{}', '{}', '{}')""".format(
                            self.version, 
                            self.path_video, 
                            self.path_text)):

            return "Config successfully registered!"            
        else:
            return "There was an error inserting the config"                  

  
    def Update(self):  
        """Update in the bd"""
        if self._execute("""update config set version = '{}',
                        path_video = '{}',path_text = '{}'""".format(
                            self.version, 
                            self.path_video, 
                            self.path_text)):

            return "Config updated successfully!"         
        else:
            return "There was an error changing the config"

  
    def Delete(self):
        """Delete in the bd"""
        if self._execute("delete from config"):

            self._clear()

            return "config deleted successfully!"       
        else:
            return "There was an error deleting the config." 
  
    def Select(self):
        """Select in the bd"""
        try:
            self._clear()

            c = self.sql.connection.cursor()

            c.execute("select  * from config")

            for line in c:
                self.version = line[0]
                self.path_video = line[1]
                self.path_text = line[2]

            c.close()
  
            return "Search done successfully!"
        except:
            return "config search error"
