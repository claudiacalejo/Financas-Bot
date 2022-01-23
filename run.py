from unittest.result import failfast
from financas.financas import WebScrapper
import financas.constants as const

#dont show logs
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


with WebScrapper(teardown=True) as bot:
    bot.land_first_page()
    bot.add_login(
        const.NUMERO_CONTRIBUINTE,
        const.PASSWORD
        )
    bot.escolher_emitir()
    bot.escolher_inquilino()
    bot.escolher_datas(
        const.DATA_INICIO,
        const.DATA_FIM,
        const.DATA_PAGAMENTO
        )
    bot.escolher_renda()
    bot.verificacao_dados()
    bot.emitir_recibo()



   
