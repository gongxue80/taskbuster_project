from selenium import webdriver
import unittest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver.exe'))
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')