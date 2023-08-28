from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


class Event(models.Model):
    """
    Events model for database.
    """
    def validate_date(date):
        if date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    content = models.TextField(blank=False)
    date = models.DateField(null=True, blank=False, validators=[validate_date])
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
