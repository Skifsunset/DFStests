import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        # navigate to home page
        cls.driver.get("https://www.fanduel.com")

    def test_login_home(self):
        driver = self.driver

        # click on Log In button
        self.assertTrue(driver.find_element_by_name("login").is_displayed())
        log_in_button = WebDriverWait(driver, 50).\
            until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Log in")))
        log_in_button.click()

        # get all the fields from Log In form
        email_field = WebDriverWait(driver, 50).\
            until(expected_conditions.visibility_of_element_located((By.ID, "email")))
        self.assertTrue(self.driver.find_element_by_id("email").is_displayed())
        password_field = driver.find_element_by_id("password")
        checkbox = driver.find_element_by_id("checkbox_remember")
        login_to_account = driver.find_element_by_name("login")

        # check max length of email textbox
        self.assertEqual("255", email_field.get_attribute("maxlength"), 'incorrect maxlength')

        # check all fields are enabled
        self.assertTrue(email_field.is_enabled() and password_field.is_enabled() and
                        checkbox. is_enabled() and login_to_account.is_enabled(),
                        'one of the elements is not enabled')

        # check the checkbox is checked
        self.assertTrue(checkbox.is_selected(), 'checkbox is not selected')

        # fill out all the fields
        email_field.clear()
        email_field.send_keys("Skifsunset@yahoo.com")
        password_field.clear()
        password_field.send_keys("testcase123")

        # uncheck the checkbox
        checkbox.click()

        # submit
        login_to_account.click()

        # confirm welcome page got loaded
        avatar = WebDriverWait(driver, 50).\
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.avatar")))
        # confirm user is logged in
        avatar.click()
        log_out_link = driver.find_element_by_css_selector(".logout-icon")
        self.assertTrue(log_out_link.is_displayed(), 'logout link is not visible')
        print "Login was successful"

    def test_login_from_Join_Now(self):
        driver = self.driver

        # wait for Join Now button to be displayed
        join_now_button = WebDriverWait(driver, 30).until(expected_conditions.
                                                          visibility_of_element_located
                                                          ((By.CSS_SELECTOR, ".largescreen-join")))

        # bring up Join Now window
        join_now_button.click()

        # click on the Log in instead
        log_in_instead = WebDriverWait(driver, 30).until(expected_conditions.
                                                         visibility_of_element_located
                                                         ((By.LINK_TEXT, "Log in instead")))
        log_in_instead.click()

        # confirm user is taken to Log In page
        self.assertEqual("https://www.fanduel.com/p/login", driver.current_url)
        print "'Log in instead' is displayed on Join Now page"

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
