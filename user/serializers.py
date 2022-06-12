from rest_framework import serializers
from .models import user


class getAllUser(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = '__all__'


class Login(serializers.Serializer):
    email = serializers.EmailField()
    matkhau = serializers.CharField(max_length=20)

class register(serializers.Serializer):
    email = serializers.EmailField()
    matkhau = serializers.CharField(max_length=20)
    bienso = serializers.CharField(max_length=20)
    loaixe = serializers.IntegerField(default=0)
