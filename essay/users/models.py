from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    username = models.CharField(blank=True, null=True,unique=True,max_length=10)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',null=True)
    name =models.CharField(max_length=50)
    dob = models.DateField()
    contact = models.IntegerField()
    STATE_CHOICES = [
        ("DELHI", "Delhi"),
        ("MUMBAI","Mumbai"),
        ("BIHAR","Bihar")
    ]
    state = models.CharField(choices=STATE_CHOICES, max_length=20)

    LANGUAGE_CHOICES = [
        ("HINDI", "Hindi"),
        ("ENGLISH", "English"),
        ("SANSKRIT", "Sanskrit")
    ]
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=15)

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHERS", "Prefer not to disclose")
    ]
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10)
