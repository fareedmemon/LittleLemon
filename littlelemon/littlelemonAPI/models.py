from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    date = models.DateTimeField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def get_item(self):
        return f"{self.title} : {self.price}"
    
    # def __str__(self) -> str:
    #     return f"{self.title} : {self.price}"