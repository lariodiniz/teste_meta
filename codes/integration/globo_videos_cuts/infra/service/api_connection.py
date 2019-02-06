#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import requests 
import json

class ApiConnection:

    def __init__(self, url = ""):
        self._url = 'http://127.0.0.1:8080/'

        if url != '':
            self._url = url

    def checks_cutting_work(self, job_id):
        try:
            r = requests.get(self._url+'api/cutting_jobs/{}/'.format(job_id))
        except ConnectionError:            
            return 'Erro de conexão'
        if r.status_code == 200:
            retorno = r.json()
            return retorno['message']

    def post_program(self, program, path):
        p = {
            'title':program.title, 
            'start_time':program.start_time, 
            'end_time':program.end_time,
            'path':path}
        headers = {'content-type': 'application/json'}
               
        try:
            r = requests.post(self._url+'api/programs/', data=json.dumps(p), headers=headers)
        except ConnectionError:
            return 'Erro de conexão'
               
        if r.status_code == 201:
           return ('success', r.json())
        else:
            return 'Erro {}'.format(r.status_code)

    def post_globo_play(self, video_process):
        p = {
            'title':video_process[0], 
            'name':video_process[1],
            'duration':video_process[2]
            }
        headers = {'content-type': 'application/json'}
               
        try:
            r = requests.post(self._url+'api/globo_play/', data=json.dumps(p), headers=headers)
        except ConnectionError:
            return 'Erro de conexão'
               
        if r.status_code == 201:
           return ('success', r.json())
        else:
            return 'Erro {}'.format(r.status_code)
