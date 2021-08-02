from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Training(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    website = models.CharField(max_length=255, default='Youtube')
    link = models.URLField(default='')
    date = models.DateField()

    def __str__(self):
        return self.title 

class Personal_Work(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    
class Waaneiza_Work(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    date = models.DateField()

    def __str__(self):
        return self.title