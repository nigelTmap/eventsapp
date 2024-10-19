from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class EventCategoryView(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class= EventCategorySerializer

class EventSubCategoryView(viewsets.ModelViewSet):
    queryset = EventSubCategory.objects.all()
    serializer_class= EventSubCategorySerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class= EventSerializer

class VenueTypeView(viewsets.ModelViewSet):
    queryset = VenueType.objects.all()
    serializer_class= VenueTypeSerializer

class VenueView(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class= VenueSerializer

class TicketTypeView(viewsets.ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class= TicketTypeSerializer

class TicketView(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class= TicketSerializer

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class= RegistrationSerializer

class AttendeeView(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class= AttendeeSerializer

class PaymentMethodView(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class= PaymentMethodSerializer

class PaymentView(viewsets.ModelViewSet):
    queryset =Payment.objects.all()
    serializer_class= PaymentSerializer
