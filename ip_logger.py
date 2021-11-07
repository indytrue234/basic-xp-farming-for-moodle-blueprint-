
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://bunam.unam.mx/incorporadas/moodle/")


username1 = input("Input your username: ")
password1 = input("Input your password: ")



username = driver.find_element_by_id("username")
username.send_keys(username1)
username.send_keys(Keys.RETURN)

password = driver.find_element_by_id("password")
password.send_keys(password1)
password.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Mis Cursos" ))
    )

    element.click()
except:
    driver.quit()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Narración y Exposición"))
    )

    element.click()
except:
    driver.quit()



#this clicks on the course
curso = driver.find_element_by_xpath("//*[@id='module-723']/div/div/div[2]/div/a/span")
curso.click()


number_repeat = float(input(" # of times on repeat "))
y = 0


# comment to input
komment = input("Input comment: ")

# this clicks on the comment button
click2 = driver.find_element_by_class_name("comment-link")
click2.click()

while y < number_repeat:

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='dlg']"))
        )

        element.click()

        element.send_keys(komment)
        element.send_keys(Keys.RETURN)

    except:
        print("no")

    time.sleep(3)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='comment-action-post']"))
        )

        element.click()
    except:
        print("no")

    time.sleep(3)

    y += 1

    print("Current loop\n")
    print(y)


















