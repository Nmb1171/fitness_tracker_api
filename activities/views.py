from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, ActivitySerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Activity

# Create your views here.



class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityListCreateView(ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only the authenticated user's activities are returned
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the authenticated user as the owner of the activity
        serializer.save(user=self.request.user)

class ActivityDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only the authenticated user's activities are accessible
        return Activity.objects.filter(user=self.request.user)

