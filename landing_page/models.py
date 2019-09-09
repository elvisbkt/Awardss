from django.db import models
import datetime as dt
from users.models import CustomUser
from django.urls import reverse
from PIL import Image as PillowImage

class Category(models.Model):
    category_name =  models.CharField(max_length=20)

    def __str__(self):
        return self.category_name





    class Meta:
        ordering = ('-posted_on',)

    def __str__(self):
        return f'{self.posted_by}'

    def save_website(self):
        '''
        method to save a posted image
        '''
        self.save() 
    def save(self, *args, **kwargs):
        '''
        method to resize image size if uploaded image is larger than 600px x 600px
        '''
        super(Website, self).save(*args, **kwargs)
        img = PillowImage.open(self.image.path)
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})

    @classmethod
    def search_by_title(cls,search_term):
        '''
        method to search for images based on what user inputs
        ''' 
        websites = cls.objects.filter(title__icontains=search_term).order_by('-posted_on')
        return websites

