import re
import os
import time
import getpass
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

keychain = {}
keychain["username"] = input("Felhasznalonev: ")
keychain["password"] = getpass.getpass()

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, service_log_path=os.devnull)
driver.get("https://aromo.poli.hu/Aromo2010/loginaromo.aspx")

usertype = driver.find_element(
    "xpath", '//*[@id="ctl00_mainContent_rUserType"]/tbody/tr[3]')
username = driver.find_element(
    "xpath", '//*[@id="ctl00_mainContent_eUserName"]')
password = driver.find_element(
    "xpath", '//*[@id="ctl00_mainContent_ePassword"]')
loginkey = driver.find_element("xpath", '//*[@id="ctl00_mainContent_btnOK"]')

time.sleep(1)

usertype.click()
username.send_keys(keychain["username"])
password.send_keys(keychain["password"])
loginkey.click()
time.sleep(1)


grdspage = driver.find_element(
    "xpath", '//*[@id="ctl00_mainMenun2"]/table/tbody/tr/td/a')
grdspage.click()

time.sleep(1)

pagesoup = BeautifulSoup(driver.page_source, features="html.parser")
driver.quit()


table = pagesoup.find('table', id='ctl00_mainContent_gErdemjegy')
grades = {}
for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 1:
        grades[columns[0].text.strip()] = []
    elif 0 < len(grades):
        grades[list(grades.keys())[-1]].append(int(columns[2].text.strip()[0]))

summed = [sum(x) / len(x) for x in list(grades.values())]
for i, n in enumerate(list(grades.keys())):
    print(f'{n}:'.ljust(36), end="")
    print(f"{round(summed[i], 2)}".ljust(4), end=" | ")
    print(" ".join([str(x) for x in list(grades.values())[i]]))

print("Teljes Átlag:".ljust(36), sum(summed) / len(summed))
