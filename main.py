from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import smtplib
import os

email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
list_of_results = []

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://kb.jobs.cz/')
free_positions = driver.find_element(By.XPATH, f"/html/body/header/div/div[1]/div/div[1]/div[2]/a")
free_positions.click()
time.sleep(7)
my_input = driver.find_element(By.CSS_SELECTOR, "#fulltext")
my_input.send_keys("incubator")
find_button = driver.find_element(By.XPATH, f'//*[@id="vacancies"]/div[1]/div/div/div/form/div[1]/div/button')
find_button.click()
time.sleep(5)
result = driver.find_elements(By.CLASS_NAME, f"vacancies__item-desc")
for element in result:
    list_of_results.append(element.text)
print(list_of_results)

for element in list_of_results:
    if element == "Data" or element == "data" or element == "DATA" or element == "Data Incubator":
        print("Send the CV!")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="sasha.melisova@gmail.com",
                            msg=f"Send CV!")
            connection.close()


driver.quit()