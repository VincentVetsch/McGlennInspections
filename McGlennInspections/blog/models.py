from django.db import models
from tinymce import models as tinymce_models


class Posts(models.Model):
    '''
        Fields for Posts Table
    '''
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bodytext = tinymce_models.HTMLField()
    timestamp = models.DateTimeField()
    tags = models.CharField(max_length=50)
    image1 = models.ImageField(
        upload_to="images/blogthumbs/",
        help_text="256x256px image"
    )

    def __unicode__(self):
        return self.title
