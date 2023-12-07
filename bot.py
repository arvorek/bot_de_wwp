# primeiro vou importar algumas coisas
from selenium import webdriver
from time import sleep


class whatsbot:
   def __init__(self):
      self.mensagem = "essa mensagem é um bot feito por Kauã da silva, meu nome é alfredo digital"
      self.grupo = ['Best friends','Amor']
      opções = webdriver.ChromeOptions()
      opções.add_argument('lang=pt-br')
      self.drive = webdriver.Chrome(executable_path=r'./chromedriver.exe')
      
   def enviar_mensagem(self):
      #<span dir="auto" title="Best friends" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr" style="min-height: 0px;">Best friends</span>
      #<div tabindex="-1" class="_3Uu1_">
      #<span data-icon="send" class="">
      for chats in self:

         chats =self.drive.find_element_by_xpath(f"//span [@title='{chats}']")
         chats.click()
         chat_box=self.drive.find_element_by_class_name('_3Uu1_')
         chat_box.click()
         chat_box.send_keys(self.mensagem)
         self.drive.find_element_by_xpath("//span[@data-icon'send' class=""]")

         