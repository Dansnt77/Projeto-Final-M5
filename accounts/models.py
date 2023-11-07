from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from students_courses.models import StudentCourse


class Account(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    my_courses = models.ManyToManyField(
        "courses.Course",
        through="students_courses.StudentCourse",
        related_name="students",
    )
