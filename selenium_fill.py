#Packages
from zillow import Zillow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Constants
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSc5hyzVSZ_-BGN7Mp72THM33JslaCtlcSyuuojXa66I53tZ4Q/viewform?usp=sf_link"
option = Options()
option.add_experimental_option("detach", True)
class SeleniumApplier(Zillow):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    def fill_the_form(self):
        """Opens the form and fills the box"""
        self.driver.get(GOOGLE_FORM)
        time.sleep(3)
        address_box = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_box = self.driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_box = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_apartment = self.link_to_apartment()
        price_apartment = self.price_for_apartment()
        address_apartment = self.address_for_apartment()
        print(link_box)
        print(price_apartment)
        # for i in range(0, len(address_apartment)):
        #     address_box.send_keys(address_apartment[i])
        #     price_box.send_keys(price_apartment[i])
        #     link_box.send_keys(link_apartment[i])
        #     time.sleep(2)
        #     self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        #     time.sleep(2)
        #     self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
        #     time.sleep(3)
say =SeleniumApplier()
say.fill_the_form()