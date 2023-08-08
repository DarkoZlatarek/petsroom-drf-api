from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Articles model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=False)
    article_link = models.URLField('Event URL', max_length=400, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order and display articles
        by most recent first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'
