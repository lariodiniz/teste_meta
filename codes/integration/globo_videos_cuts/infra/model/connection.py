#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import sqlite3

class Connection():  

    """Connection class with database"""
    
    def __init__(self, path="", name='bd.db'):
        
        self.connection = sqlite3.connect(path+name)
        self.createTable()
  
    def createTable(self):
        c = self.connection.cursor()
        
        c.execute("create table if not exists config ( version text, path_video text, path_text text )")

        c.execute("""create table if not exists files ( id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL UNIQUE, line INTEGER  )""")

        c.execute("""create table if not exists programs ( id INTEGER PRIMARY KEY, 
        title TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL, 
        duration TEXT NOT NULL, reconile_key INTEGER NOT NULL )""")

        self.connection.commit()
        c.close()