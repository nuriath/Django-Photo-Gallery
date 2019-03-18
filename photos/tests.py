from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.img= Image(name = 'land', image ='image/download_EV7vpwu.jpeg ', description ='this is a picture of land',)

    def test_instance(self):
        self.assertTrue(isinstance(self.img,Image))

def test_save_method(self):
        self.img.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

def test_delete_method(self):
        self.img.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)        