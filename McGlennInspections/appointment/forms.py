from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from appointment.models import CustomerName


class RegistrationForm(ModelForm):
    '''

    '''
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput())
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput())

    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = CustomerName
        exclude = ('user', 'slug',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That User Name is already taken, please try again.")

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not match.  Please try again.")
        return self.cleaned_data
