from django.db import models
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class UserSkill(models.Model):

    SKILL_TYPE_CHOICES = [
        ('TEACH', 'Teach'),
        ('LEARN', 'Learn'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    skill_type = models.CharField(
        max_length=10,
        choices=SKILL_TYPE_CHOICES
    )

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"