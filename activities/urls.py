from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('', views.ActivityListCreateView.as_view(), name='activity-list-create'),  # For listing and creating activities
    path('<int:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),  # For retrieving, updating, and deleting activities
]