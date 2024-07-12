from rest_framework.serializers import ModelSerializer

from .models import Todo, User


class TodoSerializer(ModelSerializer):

    class Meta:

        model = Todo
        fields = ['id','user', 'title', 'body', 'updated', 'created']
        read_only_fields = ['user', 'updated', 'created']





class UserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['userid', 'username', 'email']