from django.db import models
from inspector.models import Inspector
PHONE_TYPE = (
    ('M', 'Mobile'),
    ('H', 'Home'),
    ('W', 'Work'),
)
EMAIL_TYPE = (
    ('P', 'Personal'),
    ('W', 'Work'),
)


# TODO - Use django Auth User database for first_name, last_name, and email fields.
# TODO - Educate yourself on the META class
class CustomerName(models.Model):
    ''' Customer Information
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # TODO - uncomment email and phone
    #phone = models.ManyToManyField(CustomerPhone)
    #email = models.ManyToManyField(CustomerEmail)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class CustomerEmail(models.Model):
    ''' Customer Email
    '''
    # DONE - Add field to back link to CustomerName
    name = models.ForeignKey(CustomerName)
    email = models.EmailField(max_length=200, unique=True)
    email_type = models.CharField(max_length=50, choices=EMAIL_TYPE)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.email


class CustomerPhone(models.Model):
    ''' Customer Phone
    '''
    # DONE - Add field to back link to CustomerName
    name = models.ForeignKey(CustomerName)
    phone = models.CharField(max_length=20, unique=True)
    phone_type = models.CharField(max_length=50, choices=PHONE_TYPE)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.phone


# DONE - Merge InspectionAddress and HouseInformation together
class InspectionAddress(models.Model):
    ''' The address of the inspection
    '''
    # DONE - Add field to back link to CustomerName
    name = models.ForeignKey(CustomerName)
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
        return self.inspection_address + ' ' + self.inspection_city + ', ' + self.inspection_state + ' ' + str(self.inspection_zip)


class Appointment(models.Model):
    ''' Fields for Appointment Table
    '''
    #Customer information
    full_name = models.ForeignKey(CustomerName)
    # TODO - remove email and phone
    email = models.ForeignKey(CustomerEmail)
    phone = models.ForeignKey(CustomerPhone)
    slug = models.SlugField(blank=True)
    #Inspection Address
    inspection_address = models.ForeignKey(InspectionAddress)
    #Inspection details
    date_requested = models.DateField(auto_now=False, auto_now_add=False)
    time_requested = models.TimeField(auto_now=False, auto_now_add=False)
    #Notes
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #Tracking
    # DONE - Add the commented fields
    inspector = models.ForeignKey(Inspector, blank=True)
    inspector_notes = models.TextField(blank=True)
    accepted = models.BooleanField()
    pre_aggrement_meeting = models.BooleanField()
    inspection_completed = models.BooleanField()
    report_completed = models.BooleanField()

    def __unicode__(self):
        return self.slug

    def save(self, *args, **kwargs):
        # Creates the slug, including the foreign key's slug.
        self.slug = str(self.full_name.slug)
        # Calls the parent save()
        super(Appointment, self).save(*args, **kwargs)


# DONE - CustomerInformation doesn't have a __getitem__
# DONE - Email field pulls the first and last name
# DONE - Feedback is a little quarky, It needs to be revisited
class Feedback(models.Model):
    '''Fields for Feedback table
    '''
    customer = models.ForeignKey(CustomerName)
    email = models.ForeignKey(CustomerEmail)
    slug = models.SlugField(unique=True)
    #Address
    inspection_address = models.ForeignKey(InspectionAddress)
    #Notes
    comments = models.TextField()
    timestamp = models.DateTimeField()
    approved = models.BooleanField()

    def __unicode__(self):
        return self.slug
