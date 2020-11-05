from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = open("melodii.txt", "r")
nr = 0
while True:
    name_ss = f.readline()
    if nr == 0:
        driver = webdriver.Firefox()
        driver.get("https://bandcamp.com/") #accesare site
        nr = nr+1
    elem = driver.find_element_by_name("q")
    elem.clear

# scrie lady gaga in casuta de search si da enter
    elem.send_keys(name_ss)
    elem.send_keys(Keys.RETURN)
    assert "no results" not in driver.page_source
    time.sleep(10)

#pas 4
    driver.find_element_by_partial_link_text("https").click()
    assert "no results" not in driver.page_source
    time.sleep(10)
    #pas 5 - play a song
    driver.find_element_by_class_name("playbutton").click()
    assert "no results" not in driver.page_source
    time.sleep(500)

    if (name_ss == ""): #daca e sfarsit de fisier
        print("nu mai sunt melodii de ascultat")
        f.close()
        exit()