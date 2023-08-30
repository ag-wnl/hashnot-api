from django.contrib import admin
from django.urls import path, include
from api.views import HashnotViewSet, HashnotUserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hashnoturl', HashnotViewSet)
router.register(r'hashnotuser', HashnotUserViewSet)

urlpatterns = [

    path('', include(router.urls))

]

