from rest_framework import serializers
from .models import FacebookFollower

class FacebookFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookFollower
        fields = '__all__'