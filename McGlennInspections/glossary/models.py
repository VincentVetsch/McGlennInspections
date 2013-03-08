from django.db import models


# Create your models here.
class Terms(models.Model):
    '''Fields for Terms Table '''

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    definition = models.TextField()

    def __unicode__(self):
        return self.title
