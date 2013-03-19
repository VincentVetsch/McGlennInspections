from django.db import models
TYPE_CHOICE = (
    ('P', 'Parent'),
    ('C', 'Child'),
)


# Create your models here.
class Navigation(models.Model):
    '''
        Navigation:  This model is for creating site navigation links
    '''

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    link = models.CharField(max_length=200, blank=True)
    # Type is either parent or child
    type_of_link = models.CharField(max_length=1, choices=TYPE_CHOICE)
    # Parent of link
    parent = models.CharField(max_length=100, blank=True)
    # Level of the navigation
    level = models.IntegerField()
    div_class = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title
