from rest_framework import serializers
from api.models import Hashnot


class HashnotSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = Hashnot
        fields = "__all__" 