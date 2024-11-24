from django.urls import path
from .views import (
    OrganizationListView, OrganizationCreateView, 
    UserListView, UserCreateView, assign_role
)

urlpatterns = [
    # Organization URLs
    path('organizations/', OrganizationListView.as_view(), name='organization-list'),
    path('organizations/create/', OrganizationCreateView.as_view(), name='organization-create'),

    # User URLs
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:user_id>/assign-role/', assign_role, name='assign-role'),
]
