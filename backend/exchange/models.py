from django.db import models
from django.conf import settings
from skills.models import Skill


class ExchangeRequest(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('COMPLETED', 'Completed'),
    ]

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_requests'
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_requests'
    )

    skill_offered = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='offered_requests'
    )

    skill_requested = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='requested_requests'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.sender.username} → "
            f"{self.receiver.username} "
            f"({self.status})"
        )