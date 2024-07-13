from gc import get_objects
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .models import Todo
from .serializers import TodoSerializer, UserSerializer

# Create your views here.

# Register users to db
@api_view(['POST'])
def registerUser(request):

    data = request.data
    user = User.objects.create(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



# Get all users in the db
@api_view(['Get'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



# Get one user
@api_view(['Get'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



# Create a todo
@api_view(['POST'])
def createTodo(request):
    data = request.data
    user_id = data['user']
    user = get_object_or_404(User, id=user_id) 
    
    todo = Todo.objects.create (
        user = user,
        title = data['title'],
        body = data['body'],
    )

    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)



# Get all todos in the db
@api_view(['Get'])
def getTodos(request):
    todos = Todo.objects.all().order_by('-updated')
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)



# Get one todo
@api_view(['Get'])
def getTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)



# Edit a todo
@api_view(['Put'])
def updateTodo(request, pk):

    data = request.data
    
    todo = Todo.objects.get(id=pk)

    serializer = TodoSerializer(instance=todo, data=data, partial=True)
    print(serializer)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



# Delete todo
@api_view(['Delete'])
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Todo has been deleted.")



# List all todos of a user
@api_view(['GET'])
def getUserTodos(request, pk):
    user = get_object_or_404(User, id=pk)

    user_todos = []

    todos = Todo.objects.all()
    
    for todo in todos:
        if todo.user == user:
            user_todos.append(todo)

    print(user_todos)

    serializer = TodoSerializer(user_todos, many=True)
    return Response(serializer.data)
