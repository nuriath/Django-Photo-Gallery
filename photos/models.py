from django.db import models

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
        return self.name

    def save_category(self):
        self.save()    

    def update_category(self):
        self.update()        

    def delete_category(self):
        self.delete()    


class Image(models.Model):
    Image = models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
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
     




