from django.contrib.auth.models import User
from rest_framework import generics, viewsets

# Create your views here.
from api.models import Cleaner, Appointment
from api.serializers import CleanerSerializer, UserSerializer, AppointmentSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CleanerListCreateView(generics.ListCreateAPIView):
    serializer_class = CleanerSerializer
    queryset = Cleaner.objects.all()


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

