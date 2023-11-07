from .permissions import IsSuperUser, IsAdminUser
from courses.models import Course
from .models import StudentCourse
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from .serializers import AddStudentCourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from drf_spectacular.utils import extend_schema


class StudentCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = AddStudentCourseSerializer

    @extend_schema(operation_id="student_courses_patch", exclude=True)
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class StudentCourseDeleteView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Course.objects.all()
    serializer_class = AddStudentCourseSerializer

    def get_object(self):
        course_id = self.kwargs.get("course_id")
        student_id = self.kwargs.get("student_id")

        student_course = get_object_or_404(
            StudentCourse, course_id=course_id, student_id=student_id
        )
        return student_course

    def delete(self, request, *args, **kwargs):
        try:
            student_course = self.get_object()
            student_course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            error_message = {"detail": "this id is not associated with this course."}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)
