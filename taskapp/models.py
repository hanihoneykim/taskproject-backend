from django.db import models
from django.utils.translation import gettext_lazy as _  # gettext_lazy는 보통 _ 로 많이 구현함


class Task(models.Model):
    class TaskType(models.TextChoices):
        JOB = "JOB", _("업무")  # 코드에서 불러올 값 = db에서 쓸 값, 사용자에게 보여질 값
        HEALTH = "HEALTH", _("건강")  # gettext_lazy("건강") 과 동일한 값
        PERSONAL = "PERSONAL", _("개인")

    title = models.CharField(max_length=50, null=False)
    type = models.CharField(
        choices=TaskType.choices,
        max_length=15,
        default=TaskType.JOB,
    )
    due = models.DateTimeField(null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)


class ChecklistItem(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, null=False)
    is_checked = models.BooleanField(null=False, default=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
