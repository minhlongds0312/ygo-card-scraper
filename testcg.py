from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import os
import logging


while True:
    #Input name
    name = input('Card name (\'quit\' to exit): ')
    if name == 'quit':
        break
    namelist = name.split()
    nameurl = '%20'.join(namelist)

    #Setup web driver
    #chrome_options.add_experimental_option("detach", True)
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.headless = True
    url = f'https://www.tcgplayer.com/search/all/product?q={nameurl}&view=grid'
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    os.environ['WDM_LOG'] = "false"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= chrome_options)
    driver.get(url)



    #Scanning for the address of the information
    results = driver.find_element(By.CLASS_NAME, value ='marketplace')
    results2 = results.find_element(By.CLASS_NAME, value ='marketplace__content')
    results3 = results2.find_element(By.CLASS_NAME, value = 'search-layout')
    results4 = results3.find_element(By.XPATH, value = '//*[@id="app"]/div/section[2]/section/section/section')
    results4 = results3.find_element(By.XPATH, value = '//*[@id="app"]/div/section[2]/section/section/section/span')

    time.sleep(2) #Wait for the elements to load before continuing 

    results5 = results4.find_element(By.XPATH, value = '//*[@id="app"]/div/section[2]/section/section/section/span/section')
    results6= results5.find_elements(By.CLASS_NAME, value = 'search-result') #ElementS, for a list
    #Got a list of cards, now to find the information of each card
    i = 0
    for result in results6:
        rarity = result.find_element(By.CLASS_NAME, value = 'search-result__rarity').text
        name = result.find_element(By.CLASS_NAME, value = 'search-result__title').text
        price = result.find_element(By.CLASS_NAME, value = 'search-result__market-price').text
        print(f'{rarity} {name} | {price}')
        i+=1
        if i == 5:
            break
    
    print()
    driver.quit()
