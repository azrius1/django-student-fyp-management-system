from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class logbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + str(self.date)

    def get_absolute_url(self):
        return reverse('logbook')