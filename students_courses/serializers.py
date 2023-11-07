from rest_framework import serializers
from .models import StudentCourse
from courses.models import Course
from accounts.models import Account


class StudentCourseSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(
        max_length=150, source="student.username", read_only=True
    )
    student_email = serializers.CharField(max_length=150, source="student.email")

    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]


class AddStudentCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance, validated_data):
        students_data = validated_data.get("students_courses", [])

        student_emails = [student["student"]["email"] for student in students_data]

        students = Account.objects.filter(email__in=student_emails)

        invalid_emails = set(student_emails) - set(
            students.values_list("email", flat=True)
        )
        if invalid_emails:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(invalid_emails)}."
                },
                code="invalid",
            )

        instance.students.set(students)

        return instance
