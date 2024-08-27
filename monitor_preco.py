from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging.config
import time
import datetime
import pandas as pd

def configura_driver():
    # Configura o Driver para interação com o Chrome

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    chrome_options.add_argument('log-level=3')
    logging.warning('Aplicação inicializada')
    return driver

def acessa_website_do_produto(url, driver):
    # Acessa o site
    
    driver.get(url)
    time.sleep(5)
    return driver
    
def coleta_preco_do_produto(driver, xpath):
    # Coleta o preco do produto
    
    logging.info('Extraindo o valor do produto...')
    preco = driver.find_element(By.XPATH, xpath).text
    return preco

def cria_planilha(nome, preco, url):
    
    logging.info('Criando planilha...')
    dados = {
        'Nome': [nome],
        'Data e Hora': [datetime.datetime.now()],
        'Preço': [preco],
        'URL': [url]
    }
    
    # Adiciona os dados ao CSV
    df = pd.DataFrame(dados)
    df.to_csv('preco_produto.csv', mode='a', header=not pd.io.common.file_exists('resultado_teste_velocidade.csv'), index=False)
    
def main():
    nome = 'Macbook M1'
    url = 'https://bit.ly/3AHxnCA'
    xpath = '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span/span/span[2]'
    try:
        driver = configura_driver()
        acessa_website_do_produto(url, driver)
        preco = coleta_preco_do_produto(driver, xpath)
        cria_planilha(nome, preco, url)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()