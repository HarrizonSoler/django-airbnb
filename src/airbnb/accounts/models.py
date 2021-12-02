from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from products.models import City

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #city = models.ForeignKey(City, on_delete = models.SET_NULL, null = True)
    profile_picture = models.FileField(upload_to = "profile")

    # Python 3
    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
