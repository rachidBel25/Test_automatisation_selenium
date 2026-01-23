from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def test_01 ():

    driver = setup()

    # driver.implicitly_wait(5)
    driver.maximize_window()
    # driver.implicitly_wait(5)
    
    # Comparaison de titre avec assertions

    title = driver.title
    assert title == "OrangeHRM"

    #  utlisation des arguments

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
    print("L'assetion est faite : LE TABLEAU DE BORD A ETE VERIFIE")

     # argument pour vérifier le titre  et un test passant                                 
    print('Test est execute avec succes')
    print('le titre est : ' + title)
  

# driver = None

def setup():

    global driver
    driver = webdriver.Chrome()

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

# setup()
test_01 ()