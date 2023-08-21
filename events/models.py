from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Events model for database.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    content = models.TextField(blank=False)
    date = models.DateField(null=True, blank=False)
    time = models.TimeField(null=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order events by date of event,
        soonest first.
        """
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.date}'
