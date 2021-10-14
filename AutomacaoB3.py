import pyautogui
import webbrowser
from time import sleep
from tqdm import tqdm


class Scrapping:
    def __init__(self, name, password):
        self.name = name
        self.password = password

        self.code = input('Code: ')
        self.date = input('Date: ')

    def validarUser(self):
        numbers = range(int(10e5))
        for i in tqdm(numbers, colour='Green', desc='Processing', dynamic_ncols=False):
            pass

        if self.name == 'UserExample' and self.password == 123123:
            print('User Validation Completed')
            Scrapping.getArquivo(self)
        else:
            print('Invalid Credentials')

    @staticmethod
    def entrarSite():
        webbrowser.get('chrome').open_new_tab('https://www.google.com/')
        sleep(1)
        pyautogui.click(x=200, y=85)
        pyautogui.write('https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Index?agencia=18')
        pyautogui.press('return')

    def filtrarDados(self):
        data = self.date
        sleep(1)
        pyautogui.click(x=68, y=303)
        sleep(1)
        pyautogui.write(self.code)
        sleep(1)
        pyautogui.click(x=381, y=303)
        sleep(1)
        pyautogui.write(data)
        sleep(1)
        pyautogui.click(x=823, y=296)
        sleep(1)

    def getArquivo(self):
        xNoticia = 216
        yNoticia = 496
        for i in range(3):
            fs.entrarSite()
            sleep(5)
            fs.filtrarDados()
            pyautogui.click(xNoticia, yNoticia)
            sleep(5)
            for i2 in range(9):
                pyautogui.press('tab')
            pyautogui.press('return')
            sleep(5)
            for i3 in range(11):
                pyautogui.press('tab')
            pyautogui.press('return')
            sleep(5)
            pyautogui.click(x=19, y=44)
            print(f'News {i} already saved!')
            xNoticia += 406


if __name__ == '__main__':
    fs = Scrapping('UserExample', 123123)
    fs.validarUser()