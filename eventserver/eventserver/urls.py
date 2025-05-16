"""
URL configuration for eventserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from eventapi.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


route =routers.DefaultRouter()
route.register('users',UserViewSet,basename = 'users')
route.register('eventcategory',EventCategoryView,basename = 'eventcategory')
route.register('eventsubcategory',EventSubCategoryView,basename = 'eventsubcategory')
route.register('event',EventView,basename = 'event')
route.register('venuetype',VenueTypeView,basename = 'venuetype')
route.register('venue',VenueView,basename = 'venue')
route.register('tickettype',TicketTypeView,basename = 'tickettype')
route.register('ticket',TicketView,basename = 'ticket')
route.register('registration',RegistrationView,basename = 'registration')
route.register('attendee',AttendeeView,basename = 'attendee')
route.register('paymentmethod',PaymentMethodView,basename = 'paymentmethod')
route.register('payment',PaymentView,basename = 'payment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
