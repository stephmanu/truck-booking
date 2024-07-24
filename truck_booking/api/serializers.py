from django import forms
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import Truck, TruckBooking


class UserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
        

# Truck serializer
class TruckSerializer(ModelSerializer):
    class Meta:
        model = Truck
        fields = ['Asset_Tag', 'Truck_ID', 'Truck_Model', 'ECM_Type', 'status', 'comment']
        extra_kwargs = {"comment": {"required": False}}



        def create(self, validated_data):
            truck = Truck.objects.create(**validated_data)
            return truck


class EditTruckSerializer(ModelSerializer):
    class Meta:
        model = Truck
        fields = ['Asset_Tag', 'Truck_ID', 'Truck_Model', 'ECM_Type', 'status', 'comment']

        extra_kwargs = {"Asset_Tag": {"required": False}, "Truck_ID": {"required": False}, 
                        "Truck_Model": {"required": False}, "ECM_Type": {"required": False}, 
                        "status": {"required": False}, "comment": {"required": False}}
        


class TruckBookingSerializer(ModelSerializer):
    class Meta:

        model = TruckBooking

        fields = ['Truck_ID', 'Date', 'From_Time', 'To_Time']

        widgets = {'Date':  forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}),
                   'From_Time':  forms.TextInput(attrs={'type': 'time', 'class': 'form-control'}),
                   'To_Time':  forms.TextInput(attrs={'type': 'time', 'class': 'form-control'})}
        
        #extra_kwargs = {"Truck_ID": {"required": False}}


        #def create(self, validated_data):
        #    truckBooking = TruckBooking.objects.create(**validated_data)
        #    return truckBooking
