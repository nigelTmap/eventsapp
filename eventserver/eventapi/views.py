from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    
    @action(methods=['post'],detail=False,permission_classes = [AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response({
            'message': 'Logged in successfully'
            })
            response.set_cookie('access_token', str(refresh.access_token), httponly=True)
            response.set_cookie('refresh_token', str(refresh), httponly=True)
            return response
        return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
    

    @action(methods=['post'],detail=False,permission_classes = [AllowAny])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = Response({
            'message': 'User registered successfully'
            })
            response.set_cookie('access_token', str(refresh.access_token), httponly=True)
            response.set_cookie('refresh_token', str(refresh), httponly=True)
            return response
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

#permission_classes=[IsAuthenticated]
    @action(methods=['post'],detail=False,permission_classes = [AllowAny])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            OutstandingToken.objects.filter(token=refresh_token).delete()
            return Response({'message': 'Logged out successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['post'], detail=False)
    def token(self, request):
        token_obain_pair_view = TokenObtainPairView.as_view()
        response = token_obain_pair_view(request._request)
        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')
            response = Response({
                'access': access_token,
                'refresh': refresh_token
            })
            response.set_cookie('access_token', access_token, httponly=True)
            response.set_cookie('refresh_token', refresh_token, httponly=True)
            return response

    @action(methods=['post'], detail=False)
    def refresh_token(self, request):
        token_refresh_view = TokenRefreshView.as_view()
        response = token_refresh_view(request._request)
        if response.status_code == 200:
            access_token = response.data.get('access')
            response = Response({
                'access': access_token
            })
            response.set_cookie('access_token', access_token, httponly=True)
            return response



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
