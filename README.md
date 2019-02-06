Test Meta
=

    interface desktop feita em Python utilizando a biblioteca Tkinter e uma api feita com as bibliotecaas Django e django-rest.

- Versão Atual 0.0.1.0

Técnologias Utilizadas
-
- Python 3.7.1 
- Django
- Para mais informações veja [Requeriments](https://github.com/lariodiniz/teste_meta/blob/master/requeriments.txt) 

Funcionalidades 
-
- Analiza a entra de arquivos textos em uma pasta especificada pelo usuario enquanto a integração estiver ativa.
- informa a api de corte as informações de corte
- transfere o video cortado para uma pasta


Como executar
-
1) Instale o Git na sua maquina.
<br>Para mais informações sobre o git veja [Git](https://git-scm.com/docs).
2) faça um fork para o seu repositório Git.
3) Clone esse repositório para a sua maquina.
4) Crie uma maquina virtual com o python 3.7.1.
5) Ative a maquina virtual.
6) Vá até o diretório clonado na sua maquina.
7) Instale os Requerimentos.
<br>pip install -r requirements.txt.
8) Vá até a pasta codes/globo_videos_cuts/globo_videos_cuts e crie um arquivo local_settings usando o arquivo de exemplo como base.
9) Vá até a pasta codes/globo_videos_cuts/. 
10) Execute as migrações.
<br>python manage.py migrate
11) Inicie a api django na porta 8080.
<br>python manage.py runserver 8080
12) Vá até a pasta codes/integration/globo_videos_cuts. 
13) Execute a Aplicação de integração
<br>python Application
14) Na tela da Aplicação precionar no botão procurar do lado do campo "Pasta de txt" e selecionar a pasta onde os arquivos txt são salvos.
15) Precionar no botão salvar do lado do campo "Pasta de txt" para salvar o caminho no sistema.
16) Na tela da Aplicação precionar no botão procurar do lado do campo "Pasta video" e selecionar a pasta onde os arquivos de videos serão salvos pela api de corte.
17) Precionar no botão salvar do lado do campo "Pasta videos" para salvar o caminho no sistema.
18) Ativar o Sistema.


Como Contribuir
-
1) Instale o Git na sua maquina.
<br>Para mais informações sobre o git veja [Git](https://git-scm.com/docs).
2) faça um fork para o seu repositório Git.
3) Clone esse repositório para a sua maquina.
4) Na pasta clonada da sua maquina inicie o git flow.
<br>Para mais informações sobre o git flow veja [Git Flow](https://medium.com/@lariodiniz/tutorial-git-com-git-flow-476ad906c8ae).
5) Crie uma maquina virtual com o python 3.7.1.
6) Instale os Requerimentos.
7) Crie um braço de feature e faça suas modificações, não esqueça de fazer testes para as mesmas.
8) Ao finalizar solicite um Pull Request. 
 
Como Testar
-
1) Vá até o diretório clonado na sua maquina.
2) Com seu ambiente virtual ativado rode o comando no prompt: py.test


Licença
-
[MIT](https://github.com/lariodiniz/teste_meta/blob/master/LICENSE.md)

![Python](https://github.com/lariodiniz/teste_meta/blob/master/docs/imgs/python_logo.png)
![Django](https://github.com/lariodiniz/teste_meta/blob/master/docs/imgs/django_logo.jpg)
