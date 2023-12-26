from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class TaskType(models.TextChoices):
        JOB = "JOB", _("업무")
        HEALTH = "HEALTH", _("건강")
        PERSONAL = "PERSONAL", _("개인")

    title = models.CharField(max_length=50, null=False)
    type = models.CharField(
        choices=TaskType.choices,
        max_length=15,
        default=TaskType.JOB,
    )
    due = models.DateTimeField(null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
