from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #pass
        self.browser.quit()

    def test_start_and_save_list(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Remember to finish this test later on. See chapter 2')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    

# Edith has heard? about an online to-do app.
# She checks out its hmepage

# Edith notices the page title and header mention to-do lists

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box
# (edith's hobby is tying fly-fishing lures)

# She hits enter, the page updates. The page lists:
# "1: Buy Peacock Feathers as an item in a to-do list

# There is still a text box inviting her to add another item.
# She enters "Use peacock feathers to make a fly"
# (Edith is methodical)

# Page updates again, showing both items on the list.

# Edith wonders if the site will remember her list.
# She sees the site generates a unique URL for her -- with explanatory text
# She visits that URL and her to-do list is still there.

# Satisfied, she goes back to sleep


