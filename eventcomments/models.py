from django.db import models
from django.contrib.auth.models import User
from events.models import Event


# Class taken from DRF-API walkthrough.
class EventComment(models.Model):
    """
    Comments Model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    eventpost = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """
        Display newest comments first.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Display content instead of the ID.
        """
        return self.content
