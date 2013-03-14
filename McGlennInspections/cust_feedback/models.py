from django.db import models


# Create your models here.
class Feedback(models.Model):
    '''Fields for Posts Table'''
    #Customer Information
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    #Address
    isp_address = models.CharField(max_length=100)
    isp_city = models.CharField(max_length=50)
    isp_state = models.CharField(max_length=50)
    isp_zip = models.IntegerField()
    #Notes
    comments = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title
