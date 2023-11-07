from django.urls import path
from .views import CourseView, CourseDetailView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<uuid:pk>/", CourseDetailView.as_view()),
]
