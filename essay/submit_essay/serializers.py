from rest_framework import serializers
from .models import WriteEssay

class WriteEssaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WriteEssay
        fields = ['topic','essay_language','essay_text']
