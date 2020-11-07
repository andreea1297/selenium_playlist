from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

def play_list():
    f = open("melodii.txt", "r")
    nr = 0

# ascultare playlist
    while True:
        name_ss = f.readline()

        if (name_ss == ""): #daca e sfarsit de fisier
            print("nu mai sunt melodii de ascultat")
            f.close()
            exit()

#deschidere firefox
        if nr == 0:
            driver = webdriver.Firefox()
            driver.get("https://bandcamp.com/") #accesare site
            nr = nr+1

        elem = driver.find_element_by_name("q")
        elem.clear

# scrie numele si melodia in casuta de search si da enter
        elem.send_keys(name_ss)
        elem.send_keys(Keys.RETURN)
    #assert "no results" not in driver.page_source
        time.sleep(10) #secunde

    #pas 4

        driver.find_element_by_partial_link_text("https").click()
        #assert "no results" not in driver.page_source
        time.sleep(8) #secunde

    #pas 5 - play a song
        driver.find_element_by_class_name("playbutton").click()
        #assert "no results" not in driver.page_source
        time.sleep(250) #250 sec



#salvare in fisier a melodiilor asculate
def save_songs():
    f = open("m1.txt", "w")
    nr = 0
    mel = 0
    while True:

        if nr == 0:
            driver = webdriver.Firefox()
            driver.get("https://bandcamp.com/")  # accesare site
            nr = nr+1

        print("Acultati o melodie - dati play la melodie")
        time.sleep(30)
        print("timpul a expirat")

        nume_cantaret = driver.find_element_by_id("name-section").text
        print(nume_cantaret)

        time_current = datetime.now()
        time_mel = time_current.strftime("%H:%M:%S")
        print(time_mel)

        # scriere in fisier
        f.write(nume_cantaret,)
        f.write(" Ati ascultat melodia la ora: ")
        f.write(time_mel)
        f.write('\n')

        if (mel == 2):
            f.close()
            exit()
        time.sleep(5)
        mel = mel+1



#play_list()
save_songs()