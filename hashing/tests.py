from selenium import webdriver
from django.test import TestCase


class FunctionalTestCase(TestCase):  #Capital-camel(inherit-testcase)
    #start
    def setUp(self):
        self.browser = webdriver.Chrome()


    #coding
    def test_there_is_homepage(self):
        self.browser.get('https://localhost:8000/')
        self.assertIn('Enter hash here', self.browser.page_source)
    
    #end
    def tearDown(self):
        self.browser.quit()


