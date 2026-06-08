from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(
        max_length=255,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    profile_picture = models.URLField(blank=True, null=True)

    credits = models.IntegerField(
        default=0
    )

    trust_score = models.FloatField(
        default=0.0
    )
class Skill(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.CharField(
        max_length=100
    )
    def __str__(self):
        return self.username