from django.db import models

from booktracer.users.models import Users


class ReadingHistory(models.Model):
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="history"
    )

