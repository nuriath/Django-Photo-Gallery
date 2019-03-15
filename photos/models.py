from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()    

    def update_location(self):
        self.update()        

    def delete_location(self):
        self.delete()    

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()   

    def update_category(self):
        self.update()        

    def delete_category(self):
        self.delete()    


class Image(models.Model):
    
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'gallery/s')
    description = models.CharField(max_length =250)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()    

    def update_image(self):
        self.update()        

    def delete_image(self):
        self.delete()  

    def get_image_by_id(id):
        self.get_image_by_id()    

    def search_image(category):
        self.search_image()        

    def filter_by_location(location):
        self.filter_by_location()    
     
    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

