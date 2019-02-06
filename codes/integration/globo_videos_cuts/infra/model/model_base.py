#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from .connection import Connection
from abc import ABC, abstractmethod

class ModelBase(ABC):
    """
    Files model class
    """
  
    def __init__(self, connection = None):
        
        if connection == None:
            self.sql = Connection()
        elif type(connection) is Connection:
            self.sql = connection
        else:            
            raise ValueError("Parameter connection is not a Connection")

        self._clear()

    @abstractmethod
    def _clear(self):
        """Clear the fields"""
        pass

    def _execute(self, sql):
        """run a query in the bd"""
        try:  
            c = self.sql.connection.cursor()
            c.execute(sql)
            self.sql.connection.commit()
            c.close()  
            return True
        except:
            return False

    @abstractmethod
    def Insert(self):  
        """Insert in the bd"""
        pass
  
    @abstractmethod
    def Update(self):  
        """Update in the bd"""
        pass
  
    @abstractmethod
    def Delete(self):
        """Delete in the bd"""
        pass
  
    @abstractmethod
    def Select(self):
        """Select in the bd"""
        pass