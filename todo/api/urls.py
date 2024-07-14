from django.urls import path
from . import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Django todo API",
      default_version='v1',
      description="Django CRUD todo api documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="macmanustephen@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path("registeruser", views.registerUser, name="register-user"),

    path("users/", views.getUsers, name="get-users"),

    path("users/<str:pk>", views.getUser, name="get-user"),

    path("createtodo/", views.createTodo, name="create-todo"),

    path("todos/", views.getTodos, name="get-todos"),

    path("todos/<str:pk>", views.getTodo, name="get-todo"),

    path("todos/<str:pk>/update", views.updateTodo, name="update-todo"),

    path("todos/<str:pk>/delete", views.deleteTodo, name="delete-todo"),

    path("users/<str:pk>/todos", views.getUserTodos, name="get-user-todos"),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]

    