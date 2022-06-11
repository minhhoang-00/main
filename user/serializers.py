from rest_framework import serializers
from .models import user


class getAllUser(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = '__all__'


class setUser(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    fullname = serializers.CharField(max_length=255)
    phonenumber = serializers.IntegerField(default=0)
