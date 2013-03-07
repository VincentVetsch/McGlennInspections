from django.db import models


# Create your models here.
class Posts(models.Model):
    '''Fields for Posts Table '''

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    '''TODO - Add the following fields
        image field
    '''

    def __unicode__(self):
        return self.name
