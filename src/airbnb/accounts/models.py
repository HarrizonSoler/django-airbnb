from django.db import models

# Create your models here.
class City(models.Model):
    name = CharField(max_length = 200)
    state = models.ForeignKey(State, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length = 150)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length = 120)

    def __str__(self):
        return self.name

class Stay(models.Model):
    host =

class Account(models.Model):
    name = CharField(max_length = 170)
    email = EmailField(max_lenght = 200)
    city = models.ForeignKey(City, on_delete = models.SET_NULL, null = True)
    profile_picture = FileField(upload_to = "")
