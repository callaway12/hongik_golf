from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    hak = models.TextField(max_length=10)
    jungong = models.TextField(max_length=30)
    phone = models.TextField(max_length=10)
    gisu = models.TextField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile=Profile.objects.create(user=instance)
        # profile = profile(hak=request.POST['hak'], jungong=request['jungong'], phone=request['phone'],gisu=request['gisu'])

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


#  profile = User.objects.profile(hak=request.POST['hak'], jungong=request['jungong'], phone=request['phone'],gisu=request['gisu'])
#             profile.save()