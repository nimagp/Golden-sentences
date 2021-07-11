from django.contrib import path
from django.urls import admin, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]