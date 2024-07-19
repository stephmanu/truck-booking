from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User





class UserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user