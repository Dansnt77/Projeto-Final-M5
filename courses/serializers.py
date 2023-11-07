from rest_framework import serializers
from students_courses.serializers import StudentCourseSerializer
from contents.serializers import ContentSerializer
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(read_only=True, many=True)
    contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }
