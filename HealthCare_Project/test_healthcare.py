import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.Appointmentpage import Appointment
# service_obj = Service('C:/Users/vener/Downloads/chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)


from PageObjects.Homepage import HomePage
from PageObjects.Loginpage import LoginPage


@pytest.mark.usefixtures("setup")
class Test_Mini_project:
    def test_healthPro(self):

        homepage_object = HomePage(self.driver)
        homepage_object.MakeAppointment()
        # self.driver.find_element(By.ID,"btn-make-appointment").click()
        loginpage_object = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        loginpage_object.getusername().send_keys("John Doe")
        # driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("John Doe")

        loginpage_object.getpassword().send_keys("ThisIsNotAPassword")
        # driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys("ThisIsNotAPassword")

        loginpage_object.clicklogin().click()
        # driver.find_element(By.ID,"btn-login").click()


        # Select() -> this class  is used to get the static dropdown from the web page.

        dropdown = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "combo_facility")))
        select1 = Select(dropdown)
        select1.select_by_visible_text("Hongkong CURA Healthcare Center")

        # driver.find_element(By.ID,"chk_hospotal_readmission").click()

        Appointment_object = Appointment(self.driver)
        Appointment_object.clickcheckbox()
        WebDriverWait(self.driver, 3)

        Appointment_object.selectProgram().click()
        # driver.find_element(By.ID,"radio_program_medicaid").click()


        # driver.find_element(By.XPATH,"//textarea[@placeholder='Comment']").send_keys("Vikash is doing automation")
        WebDriverWait(self.driver, 3)
        Appointment_object.writecomment().send_keys("Vikash is doing automation")


        # driver.find_element(By.ID,"btn-book-appointment").click()
        Appointment_object.confirmation()
        print("Thankyou Vikash! Your appointment has been successfully booked.")


# dropdown = Select(driver.find_element(By.ID,"combo_facility"))
# dropdown.deselect_by_visible_text("Hongkong CURA Healthcare Center")

'''Use driver.close() when you want to close only the current window.
Use driver.quit() when you want to close all windows and clean up the WebDriver session.'''
