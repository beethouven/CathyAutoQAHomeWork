import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.by import By

logger = logging.getLogger('mylogger')
options = webdriver.ChromeOptions()
device = ['Pixel 7','iPhone 12 Pro']


def screenshot(driver, logger, reason):
   Screenshot_document = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
   path = "./screenshot/" + Screenshot_document
   path = os.path.join(path)
   if not os.path.exists(path):
      os.mkdir(path)
   file_name = reason + "_" + str(datetime.now().hour) +  str(datetime.now().minute) + str(datetime.now().second) + ".png"
   path = os.path.join(path, file_name)
   try:
      driver.get_screenshot_as_file(path)
      logger.info(file_name + 'already be saved success')
   except OSError:
      logger.error(file_name + 'failed')

def to_homepage(driver):
   driver.get('https://www.cathaybk.com.tw/cathaybk/')
   WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)

def count_creditcard_item_list(driver, logger):
   driver.find_element(By.CLASS_NAME,"cubre-o-header__burger").click()
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'產品介紹')]")))
   driver.find_element(By.XPATH,"//*[contains(text(),'產品介紹')]" ).click()
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'信用卡')]")))
   driver.find_element(By.XPATH,"//*[contains(text(),'信用卡')]" ).click()
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='cubre-o-menuLinkList__content']>a:last-child")))
   creditcard_count = driver.find_elements(By.CSS_SELECTOR,"div[class='cubre-o-menuLinkList__item is-L2open']>div[class='cubre-o-menuLinkList__content']>a")
   logger.warning("total creditcard items are " + str(len(creditcard_count)) + "items")

def creditcardlist_to_cardinfo(driver):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'卡片介紹')]")))
   driver.find_element(By.XPATH,"//*[contains(text(),'卡片介紹')]" ).click()

def count_stopcard(driver, logger):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"section[data-anchor-block='blockname06']"))).click()
   stopcard_count = driver.find_elements(By.CSS_SELECTOR,"section[data-anchor-block='blockname06']>div>div[class='cubre-o-block__component']>div>div[class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']>span")
   logger.warning("total stopcard are " + str(len(stopcard_count)) + "cards")
   return len(stopcard_count)

def screenshot_stopcard(driver,logger,stopcard_count):
   for i in range(stopcard_count):
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"section[data-anchor-block='blockname06']>div>div[class='cubre-o-block__component']>div>div[class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']>span:nth-child("+ str(i+1)+")"))).click()
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"section[data-anchor-block='blockname06']>div>div[class='cubre-o-block__component']>div>div[class='swiper-wrapper']>div:nth-child("+ str(i+1)+")"))).click()
      screenshot(driver,logger,"stopcard")
      logger.warning( str(i+1) + "th screenshot to be recorded ")

for i in device:
   options.add_experimental_option('mobileEmulation',{'deviceName':i})
   driver = webdriver.Chrome(options=options)
   to_homepage(driver)
   screenshot(driver, logger, "homepage")
   count_creditcard_item_list(driver, logger)
   screenshot(driver, logger, "count creditcard item list")
   creditcardlist_to_cardinfo(driver)
   screenshot_stopcard(driver,logger,count_stopcard(driver,logger))

driver.close()