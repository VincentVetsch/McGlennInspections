from django.db import models


class CustomerInformation(models.Model):
    ''' Customer Information
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


# DONE - Merge InspectionAddress and HouseInformation together
class InspectionAddress(models.Model):
    ''' The address of the inspection
    '''
    full_name = models.ForeignKey(CustomerInformation)
    slug = models.SlugField(unique=True)
    inspection_address = models.CharField(max_length=100)
    inspection_city = models.CharField(max_length=50)
    inspection_state = models.CharField(max_length=50)
    inspection_zip = models.IntegerField()
    square_footage = models.IntegerField()
    basement = models.BooleanField()
    crawlspace = models.BooleanField()
    garage = models.BooleanField()
    out_buildings = models.BooleanField()
    dining_room = models.BooleanField()
    living_room = models.BooleanField()
    family_room = models.BooleanField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()

    def __unicode__(self):
        return self.inspection_address

    def get_city(self):
        return self.inspection_city


class Appointment(models.Model):
    ''' Fields for Appointment Table
    '''
    #Customer information
    full_name = models.ForeignKey(CustomerInformation)
    slug = models.SlugField(unique=True)
    #Inspection Address
    inspection_address = models.ForeignKey(InspectionAddress)
    #Inspection details
    date_requested = models.DateField(auto_now=False, auto_now_add=False)
    time_requested = models.TimeField(auto_now=False, auto_now_add=False)
    #Notes
    notes = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    accepted = models.BooleanField()
    pre_aggrement_meeting = models.BooleanField()
    inspection_completed = models.BooleanField()
    report_completed = models.BooleanField()

    def __unicode__(self):
        return self.slug


# FIXME - CustomerInformation doesn't have a __getitem__
# FIXME - Email field pulls the first and last name
class Feedback(models.Model):
    '''Fields for Feedback table
    '''
    full_name = models.ForeignKey(CustomerInformation)
    email = models.ForeignKey(CustomerInformation, related_name='customer_email')
    slug = models.SlugField(unique=True)
    #Address
    inspection_address = models.ForeignKey(InspectionAddress)
    #Notes
    comments = models.TextField()
    timestamp = models.DateTimeField()
    approve = models.BooleanField()

    def __unicode__(self):
        return self.email
