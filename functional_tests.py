import unittest
from selenium import webdriver

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.host = 'http://127.0.0.1:8000'

    def tearDown(self):
        self.browser.quit()

    def test_start_page(self):
        self.browser.get(self.host)
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main()
