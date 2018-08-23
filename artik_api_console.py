# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, getpass, string

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.username = input("Username: ")
        self.pswd = getpass.getpass()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.user_id = ""
    
    def test_untitled_test_case(self):
        '''This all gets the userID and is all portable. Tested it with both my account and Daniel's'''
        username = self.username
        pswd = self.pswd
        driver = self.driver
        #go to developer page
        driver.get("https://developer.artik.cloud/api-console")
        driver.maximize_window()
        #click login
        driver.find_element_by_class_name("login").click()
        #enter username
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        # driver.find_element_by_id("email").send_keys("christian.leishman@legrand.us")
        driver.find_element_by_id("email").send_keys(username)
        #enter password
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("Intern1!")
        driver.find_element_by_id("password").send_keys(pswd)
        #click sign in
        driver.find_element_by_id("signin").submit()
        #open drop-down for get user
        driver.switch_to.frame("iFrameResizer0")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::a[3]").click()
        time.sleep(1)
        #gets the user
        driver.find_element_by_id("Get Current User Profile").click()
        #save user_id
        self.user_id = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=':'])[21]/following::span[2]").text
        self.user_id = self.user_id[1:len(self.user_id)-1]
        time.sleep(4)
        print("user_id: " + self.user_id)
        #open drop down for getting devices
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='}'])[4]/following::a[1]").click()
        time.sleep(2)
        #enter the user_id
        driver.find_element_by_id("alpaca447").click()
        driver.find_element_by_id("alpaca447").clear()
        driver.find_element_by_id("alpaca447").send_keys(self.user_id)
        #send request
        driver.find_element_by_id("Get User Devices").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
