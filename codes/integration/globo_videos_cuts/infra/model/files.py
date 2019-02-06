#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from .connection import Connection
from .model_base import ModelBase

class Files(ModelBase):
    """
    Files model class
    """
  
    def __init__(self, connection = None, **kwargs):
        super(Files, self).__init__(connection,**kwargs)


    def _clear(self):
        """Clear the fields"""

        self.id = 0
        self.name = ""
        self.line = 0     
    

    def Insert(self):  
        """Insert in the bd"""

        if self._execute("insert into files ( name, line ) values ('{}',{})".format(
            self.name, 
            self.line)):

            return "Files successfully registered!"            
        else:
            return "There was an error inserting the files"
  
    def Update(self):  
        """Update in the bd"""

        if self._execute("update `files` set name = '{}', line = {} where id = {}".format(
            self.name, 
            self.line, 
            self.id)):

            return "Files updated successfully!"           
        else:
            return "There was an error changing the files"      
         
    def Delete(self):
        """Delete in the bd"""

        if self._execute("delete from `files` where id = {}".format(self.id)):

            self._clear()

            return "files deleted successfully!"           
        else:
            return "There was an error deleting the files."  

  
    def Select(self, id):
        self._clear()
        
        try:

            c = self.sql.connection.cursor()

            c.execute("select * from files where id = {}".format(id))

            for line in c:
                self.id = line[0]
                self.name = line[1]
                self.line = line[2]

            c.close()
  
            return "Search done successfully!"
        except:
            return "files search error"

    def SelectName(self, name):
        
        try:
            self._clear()
            c = self.sql.connection.cursor()

            c.execute("select * from files where name = '{}'".format(name))

            for line in c:
                self.id   = line[0]
                self.name = line[1]
                self.line = line[2]

            c.close()
  
            return "Search done successfully!"
        except:
            return "files search error"

    def SelectAll(self):
        
        try:
            self._clear()
            
            c = self.sql.connection.cursor()

            c.execute("SELECT * FROM `files`;")

            allfiles = {}


            for line in c:
                
                    allfiles[line[1]] =[line[0], line[1], line[2]]

            c.close()
  
            return allfiles
        except:
            return "files search error"

    def LastLine(self):
        
        try:
            
            c = self.sql.connection.cursor()

            c.execute("SELECT max(line) as n FROM `files`;")

            last_line = 0

            for line in c:                
                    last_line = line[0]
            c.close()
            if type(last_line) == int:
                return last_line
            else:
                return 8
        except:
            return "files search error"