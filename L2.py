from os import close
from selenium import webdriver
import selenium 
import  time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import key_actions
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

base_url="https://asterios.tm/index.php"
Regname="Anton"
Regpass="Password32923"
Email="euromobilco@gmail.com"
driver=webdriver.Chrome(executable_path="D:\Downloads\HON\chromedriver.exe")
driver.get(base_url)
assert "Asterios" in driver.title
driver.maximize_window()
driver.implicitly_wait(3)

element=driver.find_element_by_link_text("РЕГИСТРАЦИЯ")
assert element
print("Registration is ok")
element.click()
driver.implicitly_wait(3)
login_box=driver.find_element_by_name("login")
login_box.clear()
login_box.send_keys(Regname)
login_box.send_keys(Keys.TAB)
Pass_box=driver.find_element_by_name("pass")
Pass_box.send_keys(Regpass)
Pass_box.send_keys(Keys.TAB)
Pass_confirm=driver.find_element_by_name("pass2")
Pass_confirm.send_keys(Regpass)
Pass_confirm.send_keys(Keys.TAB)
Mail=driver.find_element_by_name("email")
Mail.send_keys(Email)
driver.implicitly_wait(5)
Mail.send_keys(Keys.TAB)
driver.implicitly_wait(5)
Mail.send_keys(Keys.ENTER)
driver.implicitly_wait(3)

Capcha=driver.find_element_by_name("subscribe")
Capcha.click()
Capcha.click()
Capcha=driver.find_element_by_name("rules")
Capcha.click()
driver.implicitly_wait(5)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELCTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-audio-button']"))).click()
time.sleep(5)

driver.quit()