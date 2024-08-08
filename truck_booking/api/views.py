from . serializers import UserSerializer, TruckSerializer, EditTruckSerializer, TruckBookingSerializer
from .models import Truck, TruckBooking

from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import generics
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin


from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
)

# Create your views here.


# Register new user
class registerUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


#login user
class loginUserView(LoginView):

    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    queryset = User.objects.all()
    authentication_form = None
    redirect_authenticated_user = True
    extra_context = None


# user password reset
class PasswordResetView(PasswordResetForm):
    form_class = AuthenticationForm 
    template_name = 'registration/password_reset_form.html'
    success_url = 'registration/password_reset_done.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    #redirect('registration/password_reset_confirm.html')


# user password reset done. email sent
class PasswordResetDoneView(TemplateView):
    template_name = 'registration/password_reset_done.html'



# user password change
class PasswordChangeView(PasswordChangeForm):
    form_class = AuthenticationForm
    template_name = 'registration/password_reset_confirm.html'
    success_url = 'registration/password_reset_complete.html'
    #redirect('registration/password_reset_complete.html')


# user password reset complete message
class PasswordResetCompletetView(TemplateView):
    template_name = 'registration/password_reset_complete.html'



# User home view
class userHomeView(TemplateView):
    template_name = 'home.html'
    permission_classes = [IsAuthenticated]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

# Register new truck
class registerTruckView(generics.CreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAdminUser]



# edit truck details
class EditTruckView(generics.RetrieveAPIView, UpdateModelMixin):
    queryset = Truck.objects.all()
    serializer_class = EditTruckSerializer
    permission_classes = [IsAdminUser]
    

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



# delete truck 
class DeleteTruckView(generics.RetrieveAPIView, DestroyModelMixin):
    queryset = Truck.objects.all()
    serializer_class = EditTruckSerializer
    permission_classes = [IsAdminUser]
    

    def delete(self, request, pk):
        truck = Truck.objects.get(id=pk)
        truck.delete()
        return Response('Truck deleted successfully')
    


# view all trucks
class viewAllTrucksView(generics.ListAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Truck.objects.all()
        return queryset
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TruckSerializer(queryset, many=True)
        return Response(serializer.data)
    


# view truck bookings
class TruckBookings(generics.ListAPIView):

    #queryset = TruckBooking.objects.all()
    serializer_class = TruckBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return TruckBooking.objects.all()
        return TruckBooking.objects.filter(User=self.request.user)

    


# create new booking
class registerTruckBookingView(generics.CreateAPIView):
    queryset = TruckBooking.objects.all()
    serializer_class = TruckBookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)

        return redirect('api/user/truck_bookings/')
    



# editting a booking
class EditTruckBookingView(generics.RetrieveAPIView, UpdateModelMixin):
    queryset = TruckBooking.objects.all()
    serializer_class = TruckBookingSerializer
    permission_classes = [IsAuthenticated]
    

    def put(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')

        booking = TruckBooking.objects.get(id=pk)

        if booking.User == self.request.user or self.request.user.is_superuser or self.request.user.is_staff:
           
            return self.update(request, *args, **kwargs) 

        return Response("You are not authorised to perform this action.")


# delete truckbooking
class DeleteTruckBookingView(generics.RetrieveAPIView, DestroyModelMixin):
    queryset = TruckBooking.objects.all()
    serializer_class = EditTruckSerializer
    permission_classes = [IsAuthenticated]
    

    def delete(self, request, pk):
        booking = TruckBooking.objects.get(id=pk)

        if booking.User == self.request.user or self.request.user.is_superuser:
            booking.delete()
            return Response('Booking deleted successfully')
        
       
        return Response("You are not authorised to perform this action.")
    

