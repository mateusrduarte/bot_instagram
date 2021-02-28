from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
    
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:/Users/mateu/Documents/Workspace/instagramBot/geckodiver/geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        
        campoUsuario = driver.find_element_by_xpath("//input[@name='username']")
        campoUsuario.click()
        campoUsuario.clear()
        campoUsuario.send_keys(self.username)

        campoSenha = driver.find_element_by_xpath("//input[@name='password']")
        campoSenha.click()
        campoSenha.clear()
        campoSenha.send_keys(self.password)
        campoSenha.send_keys(Keys.RETURN)

        time.sleep(3)
        infoLogin = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
        infoLogin.click()

        driver.get("https://www.instagram.com/p/CLxfQABhcTK/") #url da pagiga

        self.comentarios()

    @staticmethod
    def digitarComentario(comentario, campoComentario):
        for letra in comentario:
            campoComentario.send_keys(letra)
            time.sleep(random.randint(1,5) / 30)

    def comentarios(self):
        driver = self.driver

        try:
            listaComentarios = ["🔥","👏","🎉","😊","🥰","😁","😄","😃","😀","🤩","😛","😜","😝","😎","🤓","😏","🤖","💀","👽","😈","🤪"]
            driver.find_element_by_class_name('Ypffh').click()
            comentarioCampo = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2,5))
            self.digitarComentario(random.choice(listaComentarios), comentarioCampo)
            time.sleep(3)
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(random.randint(30,120))
        except Exception as e:
            print(e)
            time.sleep(5)

        self.comentarios()

MateusBot = InstagramBot('mateus.balao', 'R@&%64t3')
MateusBot.login()