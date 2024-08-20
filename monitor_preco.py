from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging.config
import time

def configura_driver():
    # Configura o Driver para interação com o Chrome

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    chrome_options.add_argument('log-level=3')
    logging.warning('Aplicação inicializada')
    return driver

def acessa_website_do_produto(url, driver):
    # Configura o Driver para interação com o Chrome
    
    driver.get(url)
    time.sleep(10)
    return driver
    
def coleta_preco_do_produto(driver):
    # Coleta o preco do produto
    
    preco = driver.find_element(By.XPATH, '//*[@id=":rbo:"]/li[2]/div/div[2]/div/div/div/div[1]/span/span/span[2]')
    return preco

    
def main():
    url = 'https://www.mercadolivre.com.br/apple-macbook-air-a2337-cinza-espacial-8-gb-256-gb-2560-px-x-1600-px-apple-m1-8-core-gpu-apple-m1-macos/p/MLB17828518?product_trigger_id=MLB17828522&quantity=1'
    try:
        driver = configura_driver()
        acessa_website_do_produto(url, driver)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()