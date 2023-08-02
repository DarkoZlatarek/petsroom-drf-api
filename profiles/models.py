from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Class taken from DRF-API walkthrough.
# Some modifications have been made.
class Profile(models.Model):
    """
    Profile model for database.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default-avatar-image_smynjx',
    )
    description = models.TextField(blank=True)
    place = models.CharField(max_length=50, blank=True)

    class Meta:
        """
        Display newly created profiles first.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Changing display name from ID
        to username.
        """
        return f"{self.owner}'s profile."


# Function taken from DRF-API walkthrough.
def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a user profile,
    when a new user is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)