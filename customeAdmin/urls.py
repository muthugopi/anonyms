from django.urls import path
from .views import ShowAllUsers, ApproveUser, InvestigateUser, DeleteUser
urlpatterns = [
    path('users/', ShowAllUsers.as_view(), name='admin-dashboard'),
    # Handle users verfication 
    path('users/<int:pk>/verify', ApproveUser.as_view(), name='user-approve'),
    path('users/<int:pk>/pending', InvestigateUser.as_view(), name='user-pending'),
    path('users/<int:id>/delete/', DeleteUser.as_view(), name='user-delete'),
]