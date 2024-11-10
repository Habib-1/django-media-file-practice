from django.db import models

# Create your models here.
from django.db import models
class profile(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.first_name