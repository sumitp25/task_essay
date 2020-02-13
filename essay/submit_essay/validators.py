from django.db import models
from django.core.exceptions import ValidationError

def CheckEssayText(text):
    text_list = text.split()
    if len(text_list)<500:
        raise ValidationError("Min 500 words")
    return text