from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

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

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    credits = models.IntegerField(
        default=100  # starter credits
    )

    trust_score = models.FloatField(
        default=0.0
    )

    activity_score = models.IntegerField(
        default=0
    )

    availability = models.CharField(
        max_length=100,
        blank=True
    )
class CreditTransaction(models.Model):

    EARN = "EARN"
    SPEND = "SPEND"

    TRANSACTION_TYPES = [
        (EARN, "Earn"),
        (SPEND, "Spend"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    amount = models.PositiveIntegerField()

    type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    timestamp = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"
