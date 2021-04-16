from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common import exceptions 
import json 
import pyautogui
import time
import io
#import pandas as pd 
#from openpyxl import load_workbook
import os 

#opciones ignorar exceptuando el driver_path
otps= Options()
otps.add_argument("user-agent=Mozilla/5.0 (X11; linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)")
chrome_options = webdriver.ChromeOptions()
experimentalFlags = ['calculate-native-win-occlusion@2']
chromeLocalStatePrefs = { 'browser.enabled_labs_experiments' : experimentalFlags}
chrome_options.add_experimental_option('localState',chromeLocalStatePrefs)
driver_path = 'C:\\Users\\frigh\\OneDrive\\Escritorio\\python\\chromedriver.exe'
otps.add_argument('--no-sandbox')
driver = webdriver.Chrome(driver_path)
driver.get('https://twitter.com/home')

# Login
input_user =WebDriverWait(driver, 15).until(
(EC.presence_of_element_located((By.XPATH, "//input[@name='session[username_or_email]' and @dir='auto']")))
)
input_pass = driver.find_element(By.XPATH, '//input[@name="session[password]"]')
nombre= ""
input_user.send_keys(nombre)
password = ""
input_pass.send_keys(password)
boton = driver.find_element(By.XPATH, '//main//div[@data-testid="LoginForm_Login_Button"]//div[@dir="auto"]')
boton.click()


#La lista de seguidores del usuario que querramos extraer informacion
driver.get('https://twitter.com/@example1/followers')

#aca esta definiendo la informacion a sacar ignorar
cards1 = WebDriverWait(driver, 15).until(
(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="UserCell"]')))
)
cards = driver.find_elements(By.XPATH, '//div[@data-testid="UserCell"]') 
card = driver.find_elements(By.XPATH, '//span')

time.sleep(5)

almacenamiento= []

#definimos como almacenar los datos donde X vale la lista en donde guardaremos la informacion
def juntar(x):
    cards = driver.find_elements(By.XPATH, '//div[@data-testid="UserCell"]')
    card = driver.find_elements(By.XPATH, '//span')
    for card in cards:
        pop = card.text
        x.append(pop)
        print (len(x))

almacenamiento = []

#este valor es importante define cuantas veces usaremos el scroll
#40 scroll son equivalente a 700 cuentas aproximadamente
repeat = 40

while repeat > 0:
    try:
        juntar(almacenamiento)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        repeat = repeat -1
        continue
    except:
        break


almacenamiento = list(set(almacenamiento))
calcula = len(almacenamiento)
print (calcula)
driver.quit()
print ("terminado")
with open("facu.txt", "w", encoding='utf-8') as output_file:
   for value in almacenamiento:
       output_file.write(str(value))



