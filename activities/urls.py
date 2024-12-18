from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('activities/', views.ActivityListCreateView.as_view(), name='activity-list-create' ),
    path('activities/<int:pk>', views.ActivityDetailView.as_view(), name='activity-detail')
]