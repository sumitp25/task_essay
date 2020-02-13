from django.db import models
from users.models import User,UserProfile
from .validators import CheckEssayText
# Create your models here.

class WriteEssay(models.Model):
    detail = models.OneToOneField(UserProfile,on_delete=models.CASCADE,null=True)

    TOPIC_CHOICES=[
        ("RIGHT TO EDUCATION","Right to Education"),

        ("EFFECTS OF POLLUTION","Effects of pollution"),

        ("GROWING UP IN POVERTY","Growing up in poverty"),

        ("INTERNET INFLUENCE ON KIDS","Internet Influence on kids")
    ]
    topic = models.CharField(max_length=25,choices=TOPIC_CHOICES)

    LANGUAGE_CHOICES = [
        ("ENGLISH","English"),
        ("HINDI","Hindi")
    ]
    essay_language = models.CharField(max_length=12,choices=LANGUAGE_CHOICES,)

    essay_text = models.TextField(validators=[CheckEssayText])