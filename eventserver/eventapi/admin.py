from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
admin.site.register(User)

class EventCategoryAdmin(admin.ModelAdmin):
    search_fields=('name','description')
    ordering = ('name',)
admin.site.register(EventCategory,EventCategoryAdmin)

class EventSubCategoryAadmin(admin.ModelAdmin):
    search_fields=('name','category')
    ordering = ('name',)
admin.site.register(EventSubCategory,EventSubCategoryAadmin)

class EventAdmin(admin.ModelAdmin):
    search_fields=['name','category','date','location']
    ordering = ('name',)
admin.site.register(Event,EventAdmin)

class VenueTypeAdmin(admin.ModelAdmin):
    search_fields=['name']
    ordering = ('name',)
admin.site.register(VenueType,VenueTypeAdmin)

class VenueAdmin(admin.ModelAdmin):
    search_fields=['name','city','venuetype','address']
    ordering = ('name',)
admin.site.register(Venue,VenueAdmin)

class TicketTypeAdmin(admin.ModelAdmin):
    search_fields=['name']
    ordering = ('name',)
admin.site.register(TicketType,TicketTypeAdmin)

class TicketAdmin(admin.ModelAdmin):
    search_fields=['event','tickettype','name']
    ordering = ('name',)
admin.site.register(Ticket,TicketAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    search_fields=['registration_date','ticket','event']
admin.site.register(Registration,RegistrationAdmin)

class AttendeeAdmin(admin.ModelAdmin):
    search_fields=['name','email','phone','registration']
    ordering = ('name',)
admin.site.register(Attendee,AttendeeAdmin)

class PaymentMethodAdmin(admin.ModelAdmin):
    search_fields=['name']
    ordering = ('name',)
admin.site.register(PaymentMethod,PaymentMethodAdmin)

class PaymentAdmin(admin.ModelAdmin):
    search_fields=['registration','payment_method','payment_date']
admin.site.register(Payment,PaymentAdmin)

