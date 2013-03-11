from django.db import models


# Create your models here.
class Appointment(models.Model):
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
    #House information
    sq_footage = models.IntegerField()
    basement = models.BooleanField()
    garage = models.BooleanField()
    crawlspace = models.BooleanField()
    dining_room = models.BooleanField()
    living_room = models.BooleanField()
    family_room = models.BooleanField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    #Inspection details
    date_req = models.DateField(auto_now=False, auto_now_add=False)
    time_req = models.TimeField(auto_now=False, auto_now_add=False)
    #Notes
    notes = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title
