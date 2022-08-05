from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    upload = models.FileField(upload_to='uploads')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
