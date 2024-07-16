from django.urls import include, path
from . import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import registerUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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

    path("api/v1/user/register/", views.registerUserView.as_view(), name="register-user"),

    path("api/v1/token", TokenObtainPairView.as_view(), name="get-token"),
    
    path("api/v1/token/refresh", TokenRefreshView.as_view(), name="get-token"),

    path("api-auth/", include("rest_framework.urls")),

    path("api/v1/users/", views.getUsers, name="get-users"),

    path("api/v1/users/<str:pk>", views.getUser, name="get-user"),

    path("api/v1/createtodo/", views.createTodo, name="create-todo"),

    path("api/v1/todos/", views.getTodos, name="get-todos"),

    path("api/v1/todos/<str:pk>", views.getTodo, name="get-todo"),

    path("api/v1/todos/<str:pk>/update", views.updateTodo, name="update-todo"),

    path("api/v1/todos/<str:pk>/delete", views.deleteTodo, name="delete-todo"),

    path("api/v1/users/<str:pk>/todos", views.getUserTodos, name="get-user-todos"),

    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]

    