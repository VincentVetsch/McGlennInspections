from django.db import models


# Create your models here.
class Appointment(models.Model):
    '''Fields for Posts Table'''
#TODO -- Add the rest of the fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title
