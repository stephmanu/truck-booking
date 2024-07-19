from django.urls import include, path
from . import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views
from api.views import registerUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="Django Truck booking API",
      default_version='v1',
      description="Django Truck booking api documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="macmanustephen@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path("api/user/register/", views.registerUserView.as_view(), name="register-user"),

    path("api/user/login", views.loginUserView.as_view(), name="login-user"),

    path("api/user/home", views.userHomeView.as_view(), name='home-view'),

    path("api/token", TokenObtainPairView.as_view(), name="get-token"),

    path("api/token/refresh", TokenRefreshView.as_view(), name="get-token"),

    path("api-auth/", include("rest_framework.urls")),   

    path('api/auth/password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('api/auth/password_reset/confirm', auth_views.PasswordChangeView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path("api/user/add_truck/", views.registerTruckView.as_view(), name="register-truck"),

    path("api/user/truck_list", views.viewAllTrucksView.as_view(), name='view-all-trucks')
    
]

    