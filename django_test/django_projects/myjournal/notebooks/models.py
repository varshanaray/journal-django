from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.

class Page(models.Model):
    """ Model representing a page in a notebook """
    title = models.CharField(max_length=200, help_text='Enter the title of your entry')
    date = models.DateTimeField(auto_now=True)
    entry = models.TextField(max_length=6000, help_text='Type in your entry here')
    journal = models.ForeignKey('Notebk', on_delete=models.SET_NULL, null=True)
    
    """ String for representing the Model object. """
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('page-detail', args=[str(self.id)])

class Notebk(models.Model):
    """ Model representing a page in a notebook """
    title = models.CharField(max_length=200, help_text='Enter the title of this notebook')
    description = models.CharField(max_length=800, help_text='Enter a brief description of this notebook')
    login = models.ForeignKey('Login', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """ String for representing the Model object. """
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('notebook-detail', args=[str(self.id)])


class Login(models.Model):
    # Model representing a login 
    email = models.EmailField(help_text='Enter your email')
    password = models.CharField(max_length=15, help_text='Enter your password')

    def __str__(self):
         #String for representing the Model object. 
        return self.email
