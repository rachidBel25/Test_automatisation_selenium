import pytest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver ():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
   
    yield driver
    # print("Le test est fini") ca ne marche pas
    
    driver.quit()

@pytest.mark.parametrize(("username", "password") , [
    ("Admin", "admin123"),
    ("AdminAA", "admin123444")
    ])

def test_login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    name_box = driver.find_element(By.NAME, "username")
    
    password_box = driver.find_element(By.NAME, "password")
   
    button_submit = driver.find_element(By.XPATH, "//button[@type='submit']")

    name_box.send_keys(username)
    password_box.send_keys(password)
    time.sleep(2)
    button_submit.click()
    title = driver.title
    assert title =="OrangeHRM"
    
    # print("Le test est fini")  ca ne marche pas
