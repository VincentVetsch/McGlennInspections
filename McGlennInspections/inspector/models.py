from django.db import models
#from appointment.models import Appointment


class Phone(models.Model):
    ''' Inspector Phone numbers
    '''
    phone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.phone


class Email(models.Model):
    ''' Inspector Email addresses
    '''
    email = models.EmailField()

    def __unicode__(self):
        return self.email


# TODO - Add fields
class Credential(models.Model):
    ''' Inspector Credential
    '''
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.slug


class Inspector(models.Model):
    ''' Inspector Information
    '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.ForeignKey(Phone)
    email = models.ForeignKey(Email)
    credentials = models.ForeignKey(Credential)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
