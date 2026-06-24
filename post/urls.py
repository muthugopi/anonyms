from django.urls import path
from .views import CreatePost, ShowPost, DeletePost

urlpatterns = [
    path('create/<int:id>/', CreatePost.as_view(), name='create-post'),
    path('', ShowPost.as_view(), name='show-posts'),
    path('delete/<int:id>/', DeletePost.as_view(), name='delete-post'),
]