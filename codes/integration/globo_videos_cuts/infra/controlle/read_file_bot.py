#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from threading import Thread
import os
import requests 
import json
import time
import shutil

from ..model import Files, Pograms
from ..service import ApiConnection

class ReadFileBot:

     """class that reads the files"""
    
     def __init__(self):
          self._path_texto = ""
          self._path_video = ""
          self._ativo = False
          self._jobs = {}
          self._name_file_process = "processed_by_crop_bot"
          self._api = ApiConnection()
          self._waiting = 5
     
     def Enabled(self):
          if self._path_texto != "":
               self._ativo = True               
               thread01 = Thread(target=self._search_archive).start()
               thread02 = Thread(target=self._verify_jobs).start()

     def DefinesPath(self, path_text, path_video):
          self._path_video = path_video+"/"        
          self._path_texto = path_text+"/"


     def Desaabled(self):
          self._ativo = False

     def _search_archive(self):
          while self._ativo:
               self._search_files()
          print("Desativo")

     def _verify_jobs(self):
          while self._ativo:
               if len(self._jobs) > 0:
                    for k, job in self._jobs.items():
                         if job != 'success':
                              self._sendJobs(k)
                    self._jobs = {i:self._jobs[i] for i in self._jobs if self._jobs[i] !='success'}     
          

     def _search_files(self):

          process_files = Files().SelectAll()
          caminhos = [os.path.join(self._path_texto, nome) for nome in os.listdir(self._path_texto)]
          arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
          files = [arq for arq in arquivos if (arq.lower().endswith(".txt")) and (arq.lower() not in process_files.keys())]        
          
          for file in files:               
               self._read_file(file)          

     def _read_file(self, file):          
          file_process = Files()
          file_process.name = file.lower()         
          
          lin = file_process.LastLine() 

          with open(file, 'r') as f:
               data = f.readlines()

          pograms = []
          sucesso = True

          if len(data) > lin:               
               for line in range(lin, len(data)):
                    program = Pograms()
                    program.start_time = data[line][17:28]
                    program.end_time = data[line][40:51]
                    program.title = data[line][106:138]
                    program.duration = data[line][184:195]
                    program.reconile_key = int(data[line][279:312].strip())
                    sucesso = self._sendProgram(program)

                    if sucesso:
                         pograms.append(program)
                    
          if sucesso:
               for program in pograms:
                    program.Insert()
               file_process.line = len(data)
               file_process.Insert()

     def _sendJobs(self, job_id):
          temp = time.time() - self._jobs[job_id][0]
          if temp >= self._waiting:
               self._jobs[job_id][0] = time.time()
               retorno = self._api.checks_cutting_work(job_id)
               if retorno == 'success':
                    self._delivery(self._jobs[job_id][1])
                    self._jobs[job_id] = 'success'                   
          else:
               return False
               

     def _delivery(self, program):
          try:
               if os.path.exists("{}/{}.mp4".format(self._path_video, program.title)):
                    shutil.move("{}/{}.mp4".format(self._path_video, program.title) , "process_video")
               self._api.post_globo_play([program.title, program.title, program.duration])
          except:
               pass

     def _sendProgram(self, program):
          if program.duration_seconds < 30:
               return True
          else:
               mensagem, retorno = self._api.post_program(program, self._path_video)

               if mensagem == 'success':                    
                    self._jobs[retorno['id_job']] = [time.time(), program]
                    return True
               else:
                    return False              

               
