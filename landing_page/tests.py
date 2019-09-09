from django.test import TestCase
from .models import Website
from users.models import CustomUser

class WebsiteTestCase(TestCase):

    def setUp(self):

        #Creating user instance
        self.user1 = CustomUser(username = "Denis", email = "mwai@gmail.com", password = "qpalzm741")
        self.user1.save()

        #Creating website details and saving
        self.website1 = Website(image = 'images/Tarmac.png', title = "WebLandingPage", description = "A cool website", url = 'www.awwwards.com', posted_by = self.user1)
        self.website1.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.website1, Website))

    def test_save_method(self):
        self.website1.save_website()
        websites = Website.objects.all()
        self.assertTrue(len(websites)>0)

    def test_search_filter(self):
        self.website1.save()
        searched_websites = Website.search_by_title('WebLandingPage')
        self.assertTrue(len(searched_websites)==1)

    def tearDown(self):
        Website.objects.all().delete()
