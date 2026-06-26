from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include('core.urls')),
    path('dashboard/', include('customeAdmin.urls')),
    path('post/', include('post.urls'))
]
