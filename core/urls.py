from django.urls import path
from .views import HomePage, Rules, PrivacyPage
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('rules/', Rules.as_view(), name='rules'),
    path('privacy/', PrivacyPage.as_view(), name='privacy')
]