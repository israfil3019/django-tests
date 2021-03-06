from selenium import webdriver
from django.test import SimpleTestCase
from .forms import HashForm
from .models import Hash


# class FunctionalTestCase(SimpleTestCase):  #Capital-camel(inherit-testcase)
#     #start
#     def setUp(self):
#         self.browser = webdriver.Chrome()

#     #coding
#     def test_there_is_homepage(self):
#         self.browser.get('https://localhost:8000/')
#         self.assertIn('Enter hash here', self.browser.page_source)

#     def test_hash_of_hello(self):
#         self.browser.get('https://localhost:8000/')
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys('hello')
#         self.browser.find_element_by_name('submit').click()
#         self.assertIn(
#                 '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', 
#                 self.browser.page_source
#                 )

#     #end
#     def tearDown(self):
#         self.browser.quit()


class MyUnitTestCase(SimpleTestCase):
    def test_homepage_template(self):
        response = self.client.get('/')  # not an absolute path
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())

    def text_hash_object(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()

        pulled_hash = Hash.objects.get(
            hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
            )
        self.assertEqual(hash.hash, pulled_hash)