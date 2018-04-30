from .models import *
from .serializers import *
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class RoomList(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

# class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

# class TimeslotList(generics.ListCreateAPIView):
#     queryset = Timeslot.objects.all()
#     serializer_class = TimeslotSerializer

# class TimeslotDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Timeslot.objects.all()
#     serializer_class = TimeslotSerializer

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer