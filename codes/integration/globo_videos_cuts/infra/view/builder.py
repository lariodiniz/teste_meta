#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from tkinter import Frame, Label, Entry, Button

class Builder:
    """Class that manages the application"""

    IS_TITLE = True

    def Set_font(self):
        """Sets the default font"""
        self._owner.font = ("Verdana", "8")
        self._owner.font_title = ("Calibri", "9", "bold")   
    
    
    def Set_container(self, name, pady, padx):
        """Sets a new container"""
        self._owner.containers[name] = Frame(self._owner._window)
        self._owner.containers[name]["pady"] = pady
        self._owner.containers[name]["padx"] = padx
        self._owner.containers[name].pack()

    def Set_button(self, name, text, width, command, side = None, container_name = ""):

        if container_name == "":
            container_name = name

        if not container_name in self._owner.containers.keys():
            raise KeyError('the container "{}" does not exist. Create before you put a button on it'.format(container_name)) 

        self._owner.button[name] = Button(self._owner.containers[container_name], text=text, font=self._owner.font, width=width)
        self._owner.button[name]["command"] = command       
        
        if side == None:
            self._owner.button[name].pack()
        else:
            self._owner.button[name].pack(side=side)

    def Set_entry(self, name, width, side = None, container_name = ""):

        if container_name == "":
            container_name = name

        if not container_name in self._owner.containers.keys():
            raise KeyError('the container "{}" does not exist. Create before you put a entry on it'.format(container_name)) 

        self._owner.entrys[name] = Entry(self._owner.containers[container_name])
        self._owner.entrys[name]["width"] = width
        self._owner.entrys[name]["font"] = self._owner.font
        if side == None:
            self._owner.entrys[name].pack()
        else:
            self._owner.entrys[name].pack(side=side)

    def Set_label(self, name, text, side = None, is_title = False,  container_name = ""):
        """Sets a new label"""
        if container_name == "":
            container_name = name

        if not container_name in self._owner.containers.keys():
            raise KeyError('the container "{}" does not exist. Create before you put a label on it'.format(container_name))       


        self._owner.labels[name] = Label(self._owner.containers[container_name], text=text)
        if is_title:
            self._owner.labels[name]["font"] = self._owner.font_title 
        else:
            self._owner.labels[name]["font"] = self._owner.font 
        
        if side == None:
            self._owner.labels[name].pack()
        else:
            self._owner.labels[name].pack(side=side)

    def __init__(self, owner):  
        self._owner = owner      
        self._owner.containers = {}
        self._owner.labels = {}
        self._owner.entrys = {}
        self._owner.button = {}
