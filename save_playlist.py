from selenium import webdriver
import time

f = open("melodii_ascultate", "w")
nr = 0
while True:
    if nr == 0:
        driver = webdriver.Firefox()
        driver.get("https://bandcamp.com/")  # accesare site
        nr = nr + 1
    print("Acultati o melodie - dati play la melodie")
    time.sleep(30)
    print("timpul a expirat")

    s = driver.find_element_by_tag_name("head").find_elements_by_tag_name("title")[0].text
    assert "no results" not in driver.page_source
    print(s)
    f.write(str(s))
    f.write('\n')

    f.close()
    time.sleep(5)