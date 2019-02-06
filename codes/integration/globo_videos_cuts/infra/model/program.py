#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from .connection import Connection
from .model_base import ModelBase


class Pograms(ModelBase):
    """Class of the programs model"""
  
  
    def __init__(self, connection = None, **kwargs):
        super(Pograms, self).__init__(connection,**kwargs)
 

    def _clear(self):
        """Clear the fields"""
        self.id = 0  
        self.start_time = ''
        self.end_time = ''
        self.title = ''
        self.duration = ''        
        self.reconile_key = 0 

 
    def Insert(self):  
        """Insert in the bd"""

        if self._execute("""insert into programs 
                    ( title, start_time, end_time, duration , reconile_key) 
                        values 
                        ('{}','{}','{}','{}',{})""".format(self.title,
                                                self.start_time,
                                                self.end_time,
                                                self.duration,
                                                self.reconile_key)):

            return "Progams successfully registered!"            
        else:
            return "There was an error inserting the progams"       
  
    def Update(self):  
        """Update in the bd"""
        if self._execute("""update programs set title = '{}',
                        start_time = '{}',end_time = '{}',duration = '{}',reconile_key = {}
                        where id = {}""".format(self.id)):

            return "Progams updated successfully!"        
        else:
            return "There was an error changing the progams"              

  
    def Delete(self):
        """Delete in the bd"""
        if self._execute("delete from programs where id = {}".format(self.id)):

            self._clear()

            return "Progams deleted successfully!"      
        else:
            return "There was an error deleting the progams." 

  
    def Select(self, id):
        
        try:
            self._clear()
            c = self.sql.connection.cursor()

            c.execute("select * from progams where id = {}".format(id))

            for line in c:
                self.path = line[0]
                self.id = line[1]
                self.start_time = line[2]
                self.end_time = line[3]
                self.title = line[4]
                self.duration = line[5]       
                self.reconile_key =line[6]

            c.close()
  
            return "Search done successfully!"
        except:
            return "Progams search error"

    @property
    def duration_seconds(self):
       return int(self.duration.split(':')[1]) + (int(self.duration.split(':')[0]) * 60) 