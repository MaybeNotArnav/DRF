from django.db.models.signals import (pre_save,post_save)
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save,sender=User)
def confirmation(sender,created,instance,**kwargs):
    if created:
        instance.is_active=False
        instance.save()
    token = Token.objects.create(user=instance)
    subject = 'Please confirm your Email'
    message = f'Hi {instance.username}, to confirm your email please click on this link : http://127.0.0.1:8000/bookshelf/signup/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [instance.email,]
    send_mail(subject,message,email_from,recipient_list)

