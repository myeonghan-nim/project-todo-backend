from rest_framework import serializers
from .models import Todo, User


# serializer for deal todo
class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed', )


# serializer for deal todo list
class UserSerializer(serializers.ModelSerializer):

    todo_set = TodoSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set', )
