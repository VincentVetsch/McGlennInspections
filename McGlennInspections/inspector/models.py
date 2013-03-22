from django.db import models


class Inspector(models.Model):
    ''' Inspector Information
    '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
