from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser, IsAdminOrStudent
from .serializers import ContentSerializer
from .models import Content
from drf_spectacular.utils import extend_schema


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        # course_id = self.kwargs.get("course_id")
        # course = get_object_or_404(Course, id=course_id)
        serializer.save(course_id=self.kwargs.get("course_id"))


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrStudent]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    @extend_schema(operation_id="content_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
