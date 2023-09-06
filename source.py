from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def sendTheMessage(wait, sendingText):
    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
    ActionChains(driver).send_keys(sendingText).send_keys(Keys.RETURN).perform()

def clickTheTarget(wait, messages):
    target = 'Shreyas IND' 
    contact_path = f'//span[contains(@title,"{target}")]'
    contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_path)))
    contact.click()

    for sendingText in messages:
        sendTheMessage(wait, sendingText)

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/shrey/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 100)

target = 'Deep learning ' 
contact_path = f'//span[contains(@title,"{target}")]'
contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_path)))
contact.click()

num_messages_to_retrieve = 10

for _ in range(num_messages_to_retrieve // 10):
    driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(2)

messages = []
message_elements = driver.find_elements(By.XPATH, '//div[@class="copyable-text"][@data-pre-plain-text]')
for message_element in message_elements[-num_messages_to_retrieve:]:
    message = message_element.text
    messages.append(message)

clickTheTarget(wait, messages)

while True:
    pass
