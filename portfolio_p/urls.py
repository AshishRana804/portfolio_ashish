from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secret-admin-9842/', admin.site.urls),
    path('', include('mywork.urls')),
]
