from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken



@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        RefreshToken.for_user(instance)

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created== False:
        instance.profile.save()

# @receiver(post_save,sender=User)
# def token_gen(sender,instance,created,**kwargs):



