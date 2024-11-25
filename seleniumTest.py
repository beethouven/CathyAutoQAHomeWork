import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.by import By


logger = logging.getLogger('mylogger')

def screenshot(driver, reason):
 Screenshot_document = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
 path = "./screenshot/" + Screenshot_document
 path = os.path.join(path)
 if not os.path.exists(path):
  os.mkdir(path)
 file_name = reason + "_" + str(datetime.now().hour) +  str(datetime.now().minute) + str(datetime.now().second) + ".png"
 path = os.path.join(path, file_name)
 try:
    driver.get_screenshot_as_file(path)
    logger.warning(file_name + 'already be saved success')
 except OSError:
    logger.warning(file_name + 'failed')

options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation',{'deviceName':'Pixel 7'})
driver = webdriver.Chrome(options=options)
driver.get('https://www.cathaybk.com.tw/cathaybk/')
element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)

menu = driver.find_element(By.CLASS_NAME,"cubre-o-header__burger").click()
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'產品介紹')]")))
product = driver.find_element(By.XPATH,"//*[contains(text(),'產品介紹')]" ).click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'信用卡')]")))
creditcard = driver.find_element(By.XPATH,"//*[contains(text(),'信用卡')]" ).click()
screenshot(driver,"creditcard")
creditcard_count = driver.find_elements(By.CSS_SELECTOR,"div[class='cubre-o-menuLinkList__item is-L2open']>div[class='cubre-o-menuLinkList__content']>a")
print("total creditcard")
print(len(creditcard_count))

logger.warning("total creditcard items are " + str(len(creditcard_count)) + "items")

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'卡片介紹')]")))
cardinfo = driver.find_element(By.XPATH,"//*[contains(text(),'卡片介紹')]" ).click()

element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)
stopcard = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"section[data-anchor-block='blockname06']"))).click()

stopcard_count = driver.find_elements(By.CSS_SELECTOR,"section[data-anchor-block='blockname06']>div>div[class='cubre-o-block__component']>div>div[class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']>span")
print(len(stopcard_count))
logger.warning("total stopcard are " + str(len(stopcard_count)) + "cards")

for i in range(len(stopcard_count)):
 stopcard = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"section[data-anchor-block='blockname06']>div>div[class='cubre-o-block__component']>div>div[class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']>span:nth-child("+ str(i+1)+")"))).click()
 screenshot(driver,"stopcard")
 print( str(i+1) + "th photo")

driver.close()