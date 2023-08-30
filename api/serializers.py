from rest_framework import serializers
from api.models import Hashnot, HashnotUser


class HashnotSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = Hashnot
        fields = "__all__" 
    
class HashnotUserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = HashnotUser
        fields = "__all__"