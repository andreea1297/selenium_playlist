from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

#asculate melodii din fisier
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
        time.sleep(25) #25 sec



#salvare in fisier a melodiilor asculate

def save_songs():
    f = open("mel.txt", "w")
    nr = 0
    mel = 0
    while True:

        if nr == 0:
            driver = webdriver.Firefox()
            driver.get("https://bandcamp.com/")  # accesare site
            nr = nr+1

        print("Acultati o melodie")
        time.sleep(40)
        print("timpul a expirat")

       # print(driver.find_elements_by_class_name("track_cell").text)
        try:
            driver.find_element_by_class_name("playbutton").click()
            #if driver.find_element_by_class_name("playbutton"): # se verifica daca s-a intodus o melodie, daca nu s-a introdus nicio melodie atunci se iese din program
             #   driver.find_element_by_class_name("playbutton").click() #fac click pe butonul de play
            #else:
             #   print("nu ati introdus nicio melodie")
              #  f.close()
              #  exit()

            nume_cantaret = driver.find_element_by_id("name-section").text

            print(nume_cantaret)

            time_current = datetime.now()
            time_mel = time_current.strftime("%H:%M:%S") #cand s-a dat play la melodie
            #print(time_mel)

            # scriere in fisier
            f.write(nume_cantaret) #in fisier va scrie 2 linii pt ca in html sunt 2 subclase diferite(un h2 si un a href)
            f.write(" Ati ascultat melodia la ora: ")
            f.write(time_mel)
            f.write('\n')
        except NoSuchElementException:
           print("nu ascultati nicio melodie ")
           f.close()
           exit()




#play_list()
save_songs()