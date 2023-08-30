from django.shortcuts import render
from rest_framework import viewsets
from api.models import Hashnot
from api.serializers import HashnotSerializer


# Create your views here.
class HashnotViewSet(viewsets.ModelViewSet):
    queryset = Hashnot.objects.all()
    serializer_class = HashnotSerializer