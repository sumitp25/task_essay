from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WriteEssaySerializer
from .models import  WriteEssay
# Create your views here.

class EssayViewset(viewsets.ModelViewSet):
    queryset = WriteEssay.objects.all()
    serializer_class = WriteEssaySerializer