from django.urls import path
from . import views


urlpatterns = [

    path("registeruser", views.registerUser, name="register-user"),

    path("users/", views.getUsers, name="get-users"),

    path("users/<str:pk>", views.getUser, name="get-user"),

    path("createtodo/", views.createTodo, name="create-todo"),

    path("todos/", views.getTodos, name="get-todos"),

    path("todos/<str:pk>", views.getTodo, name="get-todo"),

    path("todos/<str:pk>/update", views.updateTodo, name="update-todo"),

    path("todos/<str:pk>/delete", views.deleteTodo, name="delete-todo"),

    path("users/<str:pk>/todos", views.getUserTodos, name="get-user-todos")
]

    