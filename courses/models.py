from django.db import models
from uuid import uuid4


class CourseStatus(models.TextChoices):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        choices=CourseStatus.choices,
        default=CourseStatus.not_started,
        max_length=11,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account", on_delete=models.PROTECT, related_name="courses", null=True
    )
