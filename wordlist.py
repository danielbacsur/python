import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Hungarian_wordlist")

list_items = driver.find_elements("tag name", "li")
list_items_text = [li.text for li in list_items]

regex = re.compile(".*\d$")
list_items_filtered = list(filter(regex.match, list_items_text))

driver.quit()

with open("szavak.txt", "w", encoding="utf-8") as file:
    for list_item in list_items_filtered:
        word = list_item.split(" ")[0]
        file.write("%s\n" % word)
