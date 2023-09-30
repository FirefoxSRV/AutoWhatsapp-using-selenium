from selenium import webdriver
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


# help(webdriver.Chrome)
options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/shrey/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")


wait = WebDriverWait(driver,100)

target = '"Shreyas IND"'
sendingText = "Hello"



contact_path = '//span[contains(@title,'+ target +')]'

contact = wait.until(EC.element_to_be_clickable((By.XPATH,contact_path)))
contact.click()


message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
message_box = wait.until(EC.element_to_be_clickable((By.XPATH,message_box_path)))

ActionChains(driver).send_keys(sendingText).send_keys(Keys.RETURN).perform()


while(True):
    pass