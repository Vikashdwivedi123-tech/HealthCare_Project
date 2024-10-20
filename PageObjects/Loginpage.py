from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    username = (By.CSS_SELECTOR,"input[name='username']")
    password = (By.XPATH,"//input[@name = 'password']")
    loginbtn = (By.ID,"btn-login")

    def getusername(self):
        return self.driver.find_element(*LoginPage.username)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clicklogin(self):
        return self.driver.find_element(*LoginPage.loginbtn)

