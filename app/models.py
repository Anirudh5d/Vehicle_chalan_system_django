from django.db import models

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateField()

    def __str__(self):
        return self.registration_number

class Chalan(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    chalan_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.vehicle} - {self.amount}"
