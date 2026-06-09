from django.db import models
from django.conf import settings


class Pod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PodMember(models.Model):
    pod = models.ForeignKey(
        Pod,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("pod", "user")


# ADD BELOW THIS LINE

class Challenge(models.Model):

    pod = models.ForeignKey(
        Pod,
        on_delete=models.CASCADE,
        related_name="challenges"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    deadline = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class ChallengeSubmission(models.Model):

    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    solution_link = models.URLField()

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            "challenge",
            "user"
        )

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.challenge.title}"
        )