import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

# set the Path
s = Service('/usr/bin/chromedriver')

# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome(service=s)

def openNasPage():

    # open FritzBoxNas
    driver.get("http://192.168.178.1/nas/#/files/JMicron-Tech-01/Backup-PC")

    # set the password
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='uiPass']")))

    # enter password
    password.clear()
    password.send_keys("rugby5049")

    # target the login button and click it
    loginButton = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


def selectBackUpFile():
    uploadButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Hinzufügen")]'))).click()

    selectBackUpFileButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(), "Dateien auswählen")]'))).click()

    fileSelector = driver.find_element_by_xpath("//input[@type='file']")

    pyautogui.hotkey('ctrl', "l")
    pyautogui.hotkey('shift','7')
    pyautogui.write('home')
    pyautogui.hotkey('shift','7')
    pyautogui.write('juljano')
    pyautogui.hotkey('shift','7')
    pyautogui.write('BackUp')
    pyautogui.hotkey('shift', '7')
    pyautogui.write('text.txt')
    time.sleep(1)
    pyautogui.press('enter')


def uploadBackUpFile():

    addButton = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()

    time.sleep(1)

    okButton = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()

    os.system("notify-send 'BackUp wurde hochgeladen!'")


if __name__ == "__main__" :
    openNasPage()
    selectBackUpFile()
    uploadBackUpFile()



