from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

def upload_location(instance,filename):
    folder = 'image'
    return "%s/%s" %(folder, filename)

class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    gender = models.CharField(max_length= 1, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to = upload_location, null=True, blank=True)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
