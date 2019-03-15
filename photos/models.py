from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    Image = models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name



