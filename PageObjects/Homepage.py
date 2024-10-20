from selenium.webdriver.common.by import By
from selenium import webdriver

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    Clickmake = (By.ID,"btn-make-appointment")

    def MakeAppointment(self):
        return self.driver.find_element(*HomePage.Clickmake).click()
