from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class EventCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EventSubCategory(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    eventmanager = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(EventSubCategory, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    status = models.CharField(max_length=100,choices=[
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
        ('canccelled','Cancelled'),
        ('completed','Completed'),
    ])
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VenueType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Venue(models.Model):
    venuetype = models.ForeignKey(VenueType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TicketType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickettype = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.tickettype.name}-{self.event.name}'

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    registration_date = models.DateField()
    status = models.CharField(max_length=100,choices=[
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled'),
        ('completed','Completed'),
        ('refunded','Refunded'),
    ])
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ticket}-{self.status}'

class Attendee(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}:Event-{self.registration.event.name}'

class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.registration.ticket.name} {self.payment_date} {self.payment_method}'

