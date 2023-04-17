from django.dispatch import receiver
from django.core.signals import post_save

from .models import User,FleetManager,SystemAdmin,Driver,Passenger
  
  
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    print("in signal")
    user_group="SystemAdmin"
    if created:
        if user_group == "SystemAdmin":
            SystemAdmin.objects.create(user=instance)
        elif user_group == "FleetManager":
            FleetManager.objects.create(user=instance)
        elif user_group == "Driver":
            Driver.objects.create(user=instance)
        elif user_group == "Passenger":
            Passenger.objects.create(user=instance)
        else:
            pass
        
   
#@receiver(post_save, sender=User) 
#def save_profile(sender, instance, **kwargs):
#       instance.profile.save()