from django.db import models

# Create your models here.
class Image(models.Model):
    Image = models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    location = models.ForeignKey(location)
    category = models.ForeignKey(category)



