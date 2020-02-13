from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import EssayViewset

router =routers.DefaultRouter()

router.register('essays',EssayViewset)

urlpatterns = [
    path('',include(router.urls))
]
