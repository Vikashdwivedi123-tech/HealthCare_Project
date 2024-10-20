from selenium import  webdriver
from selenium.webdriver.common.by import By


class Appointment:
    def __init__(self,driver):
        self.driver = driver

    # facility = (By.ID, "combo_facility")
    checkbox = (By.ID, "radio_program_medicaid")
    healthprogram = (By.ID,"radio_program_medicaid")
    comment = (By.ID,"txt_comment")
    book = (By.ID,"btn-book-appointment")

    def clickcheckbox(self):
        return self.driver.find_element(*Appointment.checkbox).click()

    def selectProgram(self):
        return self.driver.find_element(*Appointment.healthprogram)

    def writecomment(self):
        return self.driver.find_element(*Appointment.comment)

    def confirmation(self):
        return self.driver.find_element(*Appointment.book).click()

