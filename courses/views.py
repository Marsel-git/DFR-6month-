from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .serializers import CourseSerializer
from accounts.permissions import IsTeacher, IsOwnerOrAdmin


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsTeacher()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAuthenticated(), IsOwnerOrAdmin()]

        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsOwnerOrAdmin()]

        return [IsAuthenticated()]