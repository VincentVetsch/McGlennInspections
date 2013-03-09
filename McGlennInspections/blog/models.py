from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Posts(models.Model):
    '''Fields for Posts Table'''
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    tags = TaggableManager()
    image1 = models.ImageField(upload_to="images/blogthumbs/", help_text="256x256px image")

    def __unicode__(self):
        return self.title
