from django.db import models
from django.contrib.auth.models import User


# Class taken from DRF-API walkthrough.
# Modifications have been made.
class Post(models.Model):
    """
    Posts Model related to Owner/User.
    """
    dog_breed_choices = [
        ('german_shepherd', 'German Shepherd'),
        ('bulldog', 'Bulldog'),
        ('labrador_retriever', 'Labrador Retriever'),
        ('golden_retriever', 'Golden Retriever'),
        ('french_bulldog', 'French Bulldog'),
        ('siberian_husky', 'Siberian Husky'),
        ('alaskan_malamute', 'Alaskan Malamute'),
        ('poodle', 'Poodle'),
        ('chihuahua', 'Chihuahua'),
        ('border_collie', 'Border Collie'),
        ('dachshund', 'Dachshund'),
        ('terrier', 'Terrier'),
        ('rottweiler', 'Rottweiler'),
        ('australian_shepherd', 'Australian Shepherd'),
        ('bichon_frisé', 'Bichon Frisé'),
        ('chow_chow', 'Chow Chow'),
        ('pomeranian', 'Pomeranian'),
        ('cavalier_king_charles_spaniel', 'Cavalier King Charles Spaniel'),
        ('english_cocker_spaniel', 'English Cocker Spaniel'),
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
    dog_breed = models.CharField(
        max_length=30,
        choices=dog_breed_choices,
        default='none'
    )

    class Meta:
        """
        Order posts by date created.
        Display by most recent first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'