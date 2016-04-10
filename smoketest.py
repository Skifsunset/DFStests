import unittest
from xmlrunner import xmlrunner
from login import LoginTests
from intropagetests import IntroPageTests

# get all tests from LoginTests and IntroPageTests class
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
intro_page_test = unittest.TestLoader().loadTestsFromTestCase(IntroPageTests)

# create test suit combining login_tests and into_page_test
smoke_tests = unittest.TestSuite([login_tests, intro_page_test])

# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)