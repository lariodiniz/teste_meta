#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from tkinter import Tk, LEFT, filedialog, END
from tkinter import messagebox

from infra.view import Builder
from infra.model import Config
from infra.controlle import ReadFileBot

__version__ = '0.0.1'

class Application():

    """Class that manages the application"""

    def _configWinow(self):
        self._config = Config()
        self._config.Select()
        if self._config.version == "":
            self._config.version = __version__
            self._config.Insert()

        self._window.title('Videos Cuts - V'+__version__)
        self._window.resizable(width=False, height=False)
        self._window.iconbitmap(r'img\\ico.ico')           

    def __init__(self, window):

        self._window = window
        self._configWinow() 
        self.bot = ReadFileBot()      


        self._builder = Builder(self)        
        
        self._builder.Set_font()

        self._builder.Set_container("title", 10, 5)
        self._builder.Set_label("title", "Videos Cuts", None, Builder.IS_TITLE)

        self._builder.Set_container("message", 5, 10)
        self._builder.Set_label("message", "")        

        self._builder.Set_container("path_text", 10, 2)
        self._builder.Set_label("path_text", "Pasta de txt: ",LEFT)
        self._builder.Set_entry("path_text", 50, LEFT)
        self._builder.Set_button("path_text_Definir", "Pocurar", 8, self._search_path_text, LEFT, "path_text")
        self._builder.Set_button("path_text_Salvar", "Salvar", 8, self._save_path_text, LEFT, "path_text")

        self._builder.Set_container("path_video", 10, 2)
        self._builder.Set_label("path_video", "Pasta video: ",LEFT)
        self._builder.Set_entry("path_video", 50, LEFT)
        self._builder.Set_button("path_video_Definir", "Pocurar", 8, self._search_path_video, LEFT, "path_video")
        self._builder.Set_button("path_video_Salvar", "Salvar", 8, self._save_path_video, LEFT, "path_video")

        self._builder.Set_container("painel_buttons", 20, 5)
        self._builder.Set_button("painel_buttons_ativar", "Ativar", 10, self._enable_bot, LEFT, "painel_buttons")
        self._builder.Set_button("painel_buttons_desativar", "Desativar", 10, self._disable_bot, LEFT, "painel_buttons")
        self._builder.Set_button("painel_buttons_sair", "Sair", 10, self._quit, LEFT, "painel_buttons")        

        
        if  (self._config.path_text !="") and (self._config.path_video !=""):
            self.entrys["path_text"].insert(0, self._config.path_text)
            self.entrys["path_video"].insert(0, self._config.path_video)
            self._enable_bot()
        else:
            self._disable_bot()


    def _search_path_text(self):         
        """search the folder path where the text files are saved"""        
        
        self.entrys["path_text"].delete(0, END)
        self.entrys["path_text"].insert(0,filedialog.askdirectory(parent=root, initialdir='/', title='Selecione o diretóio de aquivos.'))
    
    def _save_path_text(self): 
        """save the path of the folder where the text files are saved"""

        path = self.entrys["path_text"].get()

        if path == "":
            messagebox.showerror("Erro", "Selecione um caminho para salvar.")
        else:
            
            self._config.path_text = self.entrys["path_text"].get()
            result = self._config.Update()    
            
            if result == "Folder successfully registered!":
                messagebox.showinfo("Informação", "Caminho salvo com sucesso.")

    def _search_path_video(self):         
        """search the folder path where the text files are saved"""        
        
        self.entrys["path_video"].delete(0, END)
        self.entrys["path_video"].insert(0,filedialog.askdirectory(parent=root, initialdir='/', title='Selecione o diretóio de aquivos.'))
    
    def _save_path_video(self): 
        """save the path of the folder where the text files are saved"""

        path = self.entrys["path_video"].get()

        if path == "":
            messagebox.showerror("Erro", "Selecione um caminho para salvar.")
        else:
            
            self._config.path_video = self.entrys["path_video"].get()
            result = self._config.Update()    
            
            if result == "Folder successfully registered!":
                messagebox.showinfo("Informação", "Caminho salvo com sucesso.")

    def _enable_bot(self): 
        """enable read file bot"""

        self._config.Select()
        path_text = self._config.path_text
        path_video = self._config.path_video

        if path_text == "":
            messagebox.showerror("Erro", "Não existe diretório de corte salvo para a ativação do bot")
        elif path_video == "":
            messagebox.showerror("Erro", "Não existe diretório de video a ser gerado")
        else:
            self.containers["message"]["background"] = "green"
            self.labels["message"]["background"] = "green"
            self.labels["message"]["fg"] = "white"           
            self.labels["message"]["text"] = "Ativo."
            self.bot.DefinesPath(path_text, path_video)
            self.bot.Enabled()

    def _disable_bot(self):
        """disable read file bot"""
        self.bot.Desaabled()
        self.containers["message"]["background"] = "red"
        self.labels["message"]["background"] = "red"
        self.labels["message"]["fg"] = "white"
        self.labels["message"]["text"] = "Desativado."

    def _quit(self):
        self._disable_bot()
        self._window.destroy()


            
if __name__ == '__main__':
    root = Tk()

    Application(root)
    root.mainloop() 




