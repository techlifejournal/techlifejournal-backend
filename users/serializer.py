from django.db.models import fields
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name  =  serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ('email', 'full_name','user_name' , 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email' , 'full_name' , 'user_name' , 'about')

class AuthorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name' , 'user_name')