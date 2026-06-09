from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Review(models.Model):

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_given'
    )

    reviewed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_received'
    )

    rating = models.IntegerField(
    validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ]
)

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def clean(self):
        if self.reviewer == self.reviewed_user:
            raise ValidationError(
                "Users cannot review themselves."
            )

    def __str__(self):
        return (
            f"{self.reviewer.username} → "
            f"{self.reviewed_user.username} "
            f"({self.rating}/5)"
        )