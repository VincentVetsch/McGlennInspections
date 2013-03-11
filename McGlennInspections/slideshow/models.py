from django.db import models


# Create your models here.
class Slide(models.Model):
    '''
        Fields for Slide Table
    '''
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to="images/slideshow/", help_text="600x400px image")

    def __unicode__(self):
        return self.title
