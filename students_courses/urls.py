from django.urls import path
from .views import StudentCourseView, StudentCourseDeleteView

urlpatterns = [
    path("courses/<uuid:pk>/students/", StudentCourseView.as_view()),
    path(
        "courses/<uuid:course_id>/students/<uuid:student_id>/",
        StudentCourseDeleteView.as_view(),
    ),
]
