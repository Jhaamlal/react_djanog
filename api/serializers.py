from typing_extensions import Required
from django.db import models
from django.db.models import fields
# from django.db.models import fields
from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

from rest_framework.authtoken.views import Token


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        # This is stop showing password and you can only write
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

        # Create hash password
    def create(self, validated_data):
        user = User.objects.crete_user(**validated_data)
        # Token Creation as register as user register
        Token.objects.create(user=user)
        return user

    # Create token when user register
