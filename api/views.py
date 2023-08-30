from django.shortcuts import render
from rest_framework import viewsets
from api.models import Hashnot, HashnotUser
from api.serializers import HashnotSerializer, HashnotUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class HashnotViewSet(viewsets.ModelViewSet):
    queryset = Hashnot.objects.all()
    serializer_class = HashnotSerializer

    #to get all posts by a user by a custom call
    # hashnoturl/user_id/posts
    @action(detail=True, methods=['get'])
    def posts(self, request, primary_key = None):
        
        try:
            hashnot_user = Hashnot.objects.get(primary_key = primary_key)
            posts = HashnotUser.objects.filter(op_user = hashnot_user)
            posts_seralizer = HashnotUserSerializer(posts, many=True, context={'request' : request})
            return Response(posts_seralizer.data)
        except Exception as e:
            print(e)
            return Response({
                'message' : 'User might not exist.'
            })


class HashnotUserViewSet(viewsets.ModelViewSet):
    queryset = HashnotUser.objects.all()
    serializer_class = HashnotUserSerializer