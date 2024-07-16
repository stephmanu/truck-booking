from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User

from .models import Todo


class TodoSerializer(ModelSerializer):

    class Meta:

        model = Todo
        fields = ['id','author', 'title', 'body', 'updated', 'created']
        extra_kwargs = {"author": {"read_only": True}}




class UserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user