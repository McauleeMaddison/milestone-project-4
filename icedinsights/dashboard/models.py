from django.db import models
from django.contrib.auth.models import User

class CoffeeTrend(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Active' if self.active else 'Inactive'}"
