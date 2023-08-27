from django.db import models
from django.contrib.auth.models import User


# Class taken from DRF-API walkthrough.
# Modifications have been made.
class Post(models.Model):
    """
    Posts Model related to Owner/User.
    """
    pet_choices = [
        ('dog', 'dog'),
        ('cat', 'cat'),
        ('rabbit', 'rabbit'),
        ('hamster', 'hamster'),
        ('bird', 'bird'),
        ('ferret', 'ferret'),
        ('reptile', 'reptile'),
        ('fish', 'fish'),
        ('horse', 'horse'),
        ('spider', 'spider'),
        ('frog', 'frog'),
        ('gerbil', 'gerbil'),
        ('chicken', 'chicken'),
        ('duck', 'duck'),
        ('cow', 'cow'),
        ('pig', 'pig'),
        ('guinea_pig', 'guinea pig'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_image_rwq55u',
        blank=True
    )
    pet = models.CharField(
        max_length=30,
        choices=pet_choices,
        default='none',
        blank=False
    )

    class Meta:
        """
        Order posts by date created.
        Display by most recent first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
