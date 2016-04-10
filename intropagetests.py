import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod


class IntroPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        # navigate to application Intro page
        cls.driver.get("https://www.fanduel.com/")

    def test_join_now(self):
        # check Join Now button exists on Intro page
        self.assertTrue(self.is_element_present(By.XPATH, "//a[@href='#']"))
        print "Join Now button is visible"

    def test_promo_signup(self):
        # check promo signup link is displayed
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".trigger-promo-signup"))
        print "Promo SignUp is visible"

    def test_logo(self):
        # check logo is displayed
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "i.logo-fanduel"))
        print "Logo is visible"

    def test_help_link(self):
        # check help link is present
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[@href='/support'])[1]"))
        print "Help link is visible"

    def test_sections(self):
        # check all section are present including hidden one
        sections = self.driver.find_elements_by_css_selector("section.CONTENT")
        self.assertEqual(9, len(sections), 'a section is missing')
        print "All 8 sections are displayed including hidden one"

    def test_terms_section(self):
        # check terms section is visible
        WebDriverWait(self.driver, 20).\
            until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".terms")))
        print "Terms section is visible"

    def test_footer(self):
        # check all footer elements are visible
        driver = self.driver
        WebDriverWait(driver, 30).\
            until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "section.footer-links")))
        WebDriverWait(driver, 30).\
            until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "section.footer-extras")))
        WebDriverWait(driver, 30).\
            until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".footer-partners")))
        WebDriverWait(driver, 30).\
            until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".footer-copyright-links")))

        print "Footer is visible"

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param how: By locator type
        :param what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)
