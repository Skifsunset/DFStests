import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class FacebookShare(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		global driver
		driver = webdriver.Firefox()
		driver.get("https://www.fanduel.com/")
		driver.maximize_window()		

	def test_facebook_share(self):
		#Locators
		fbSharingLinkLocator = "//a[@href='https://facebook.com/fanduel']"

		fbSharingLinkElement = WebDriverWait(driver,10).\
		until(lambda driver: driver.find_element_by_xpath(fbSharingLinkLocator))

		# Get the main window handle
		mainWindowHandle = driver.window_handles

		# click the "Facebook Sharing" link
		fbSharingLinkElement.click()
		allWindowHandlesList = driver.window_handles
		for handle in allWindowHandlesList:
			if handle != mainWindowHandle[0]:
				driver.switch_to.window(handle)
				break
		WebDriverWait(driver,10).\
		until(lambda driver: driver.find_element_by_css_selector(".fb_logo"))

	@classmethod
	def tearDownClass(cls):
		driver.quit()

if __name__== '__main__':
	unittest.main(verbosity=2)	


			



	
			

