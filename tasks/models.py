from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)  # Idagdag ang field na ito
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
