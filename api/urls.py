from django.contrib import admin
from django.urls import path, include
from api.views import HashnotViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hashnoturl', HashnotViewSet)

urlpatterns = [

    path('', include(router.urls))

]