from django.db import models


class RValue(models.Model):
    '''Fields for Posts Table'''
    material = models.CharField(max_length=100)
    r_value = models.CharField(max_length=100)
    density = models.CharField(max_length=50)
    perm = models.CharField(max_length=50)
    absorbtion = models.CharField(max_length=50)
    flamespread = models.CharField(max_length=50)
    smoke = models.CharField(max_length=50)
    toxicity = models.CharField(max_length=50)
    agingeffect = models.TextField()
    timestamp = models.DateTimeField()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title
