from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)  # Equivalent to int(11) with a key symbol
    Name = models.CharField(max_length=255)  # Equivalent to varchar(255)
    No_of_guests = models.IntegerField()     # Equivalent to int(6)
    BookingDate = models.DateTimeField()     # Equivalent to datetime

    def __str__(self):
        return f"{self.Name} - {self.BookingDate}"
    
class Menu(models.Model):
    ID = models.AutoField(primary_key=True) 
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f"{self.Title} - {self.Price}"