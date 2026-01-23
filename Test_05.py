from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#  TEST foncionne en utilisant des appels fonctions
# identifiant ="Admin "          ca marche aussi en les mettant ici
# motdepasse ="admin123"
def test_01 ():

    driver = setup()

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.implicitly_wait(5)

    print("Le test 1 est termine")
    # capture d ecran
    driver.save_screenshot("test_01_screenshot.png")
    teardown(driver)
    
    # Comparaison de titre avec assertions

time.sleep(3)

def test_02():

    driver = setup()

    title = driver.title
    assert title == "OrangeHRM"
    print("Le titre est : " + title)
    print("Le test 2 est termine")

    # capture d ecran
    driver.save_screenshot("test_02_screenshot.png")

    teardown(driver)


def test_03():

    driver = setup()

    identifiant ="Admin "
    motdepasse ="admin123"

    driver.implicitly_wait(5)
    # Trouver le locators username
    name_box = driver.find_element(By.NAME, "username")
    driver.implicitly_wait(5)
    name_box.send_keys(identifiant)

    driver.implicitly_wait(6)
    # Trouver le locators password
    password_box = driver.find_element(By.NAME, "password")
    driver.implicitly_wait(6)
    password_box.send_keys(motdepasse)

    button_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_submit.click()

    #  Obtenir et verifier le tableau de bord avec le lien hyper text

    daschboard = driver.find_element(By.LINK_TEXT, "Dashboard")
    daschboard_text = daschboard.text
    Expect_text= "Dashboard"
    assert daschboard_text ==  Expect_text

      # capture d ecran
    driver.save_screenshot("test_03_screenshot.png")
    print("L'assertion a ete validéé : LE TABLEAU DE BORD A ETE VERIFIE")                             
    print("Le test 3 est terminé")
   
    teardown(driver)

def setup():
    
    global driver
   
    driver = webdriver.Chrome()

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.implicitly_wait(5)
    # WebDriverWait(driver,1000).until(lambda driver:False)
    return driver

def teardown(driver):
    driver.quit() 

# setup()    je le mets en commentaire car ça m'ouvre deux fois le naviateur   ( sur github, ils l'on met)
test_01 ()
test_02()
test_03()

# python selenium_01/Test_05.py