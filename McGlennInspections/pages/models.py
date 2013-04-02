from django.db import models
from tinymce import models as tinymce_models


class HomePage(models.Model):
    name = models.CharField(max_length=100)
    the_url = models.CharField(max_length=200)
    the_page = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.name
