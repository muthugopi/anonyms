from django.urls import path
from .views import LoginView, LogoutView, Signup, PendingPage

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
    path('pending/', PendingPage.as_view(), name='pending')
]