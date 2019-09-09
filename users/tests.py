from django.test import TestCase
from .models import CustomUser, Profile

class UserTestClass(TestCase):

    def setup (self):

        #Creating user instance
        self.user1 = CustomUser(username = "Denis", email = "mwai@gmail.com", password = "qpalzm741")
        self.user1.save()

        #Creating profile details
        self.profile1 = Profile(user=self.user1, bio='I am a test user', image= 'prof_pics/default.png')
        self.profile1.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.user1, CustomUser))

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.profile1, Profile))

    def tearDown(self):
        Profile.objects.all().delete()


