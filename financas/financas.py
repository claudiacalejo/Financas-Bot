import financas.constants as const
import os
from selenium import webdriver


class WebScrapper(webdriver.Chrome):
    def __init__(self, driver_path = r"D:\SeleniumDrivers", teardown = False): #you may have to change the path of the selenium drivers
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(WebScrapper, self).__init__()
        #wait until the element of the website is ready
        self.implicitly_wait(15)
        self.maximize_window()

    #automaticaly close the browser
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    #lands the bot in the base url defined in the constants
    def land_first_page(self):
        self.get(const.BASE_URL)

    #Login in
    def add_login(self, login_username, login_password):
        username_login = self.find_element_by_id('username')
        username_login.send_keys(login_username)
        
        password_login = self.find_element_by_id('password-nif')
        password_login.send_keys(login_password)

        login_btn = self.find_element_by_id('sbmtLogin')
        login_btn.click()

    #Choose - Emitir Recibo
    def escolher_emitir(self):
        escolher_emitir_btn = self.find_element_by_class_name('margin-top-sm')
        escolher_emitir_btn.click()

    #Choose which person
    def escolher_inquilino(self):
        escolher_inquilino_btn = self.find_elements_by_css_selector("button[onclick^='javascript:executeAction']")
        #Which button's position we want to click - we can change [1] to other number depending who we want
        escolher_inquilino_btn[1].click()

    #Select dates
    def escolher_datas(self, data_inicio_renda, data_fim_renda, data_pagamento):
        #1st day of the month
        inicio_renda = self.find_element_by_name('dataInicio')
        inicio_renda.send_keys(data_inicio_renda)
        #last day of the month
        fim_renda = self.find_element_by_name('dataFim')
        fim_renda.send_keys(data_fim_renda)
        #payment's day
        pagamento_renda = self.find_element_by_name('dataRecebimento')
        pagamento_renda.send_keys(data_pagamento)

    #Select "Renda"'s payment
    def escolher_renda(self):
        escolher_renda_radio = self.find_element_by_name('10')
        escolher_renda_radio.click()
    
    #Check if all values are right
    def verificacao_dados(self):
        print(" --- CONFIRME OS RESULTADOS! ---")
        #Name
        nome_inquilino_confirmacao = self.find_element_by_xpath('//*[@id="ng-app"]/div[5]/div[4]/div/div/table/tbody/tr/td[1]/div[1]/div[1]/div/div/span').text
        print(f"Nome inquilino ----------> {nome_inquilino_confirmacao}")
        #Dates
        data_inicio_confirmacao = self.find_element_by_xpath('//*[@id="ng-app"]/div[5]/div[7]/div/div/div[2]/div[1]/div[1]/div/input').get_attribute('value')
        print(f"Data Inicio ----------> {data_inicio_confirmacao}")
        data_fim_confirmacao = self.find_element_by_xpath('//*[@id="ng-app"]/div[5]/div[7]/div/div/div[2]/div[1]/div[2]/div/input').get_attribute('value')
        print(f"Data Fim ----------> {data_fim_confirmacao}")
        data_pagamento_confirmacao = self.find_element_by_xpath('//*[@id="ng-app"]/div[5]/div[7]/div/div/div[2]/div[1]/div[3]/div/div/input').get_attribute('value')
        print(f"Data Pagamento ----------> {data_pagamento_confirmacao}")
        #If renda's is selected
        titulo_pagamento_confirmacao = self.find_element_by_name('10').is_selected()
        if titulo_pagamento_confirmacao == True:
            print(f"Renda ----------> Correto")
        else:
            print("Renda ----------> Errado")
        #price
        valor_confirmacao = self.find_element_by_xpath('//*[@id="ng-app"]/div[5]/div[7]/div/div/div[2]/div[3]/div/div/div/div/input').get_attribute('value')
        print(f"Valor da renda ----------> {valor_confirmacao}")

    def emitir_recibo(self):
        aceitar_dados = input("Aceita emitir o recibo? ")
        if aceitar_dados == "Sim" or aceitar_dados == "sim":
            emitir_btn = self.find_element_by_xpath('//*[@id="ng-app"]/div[2]/div/div[1]/div[2]/button')
            emitir_btn.click()
            emitir_btn_confirmar = self.find_element_by_xpath('//*[@id="modalEmitirRecibo"]/div/div/div[3]/button[2]')
            emitir_btn_confirmar.click()
            print( " --- RECIBO EMITIDO ---")
        else:
            print(" --- RECIBO NÃO EMITIDO --- ")
        
        

