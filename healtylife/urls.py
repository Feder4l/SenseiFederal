
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('',include('pages.urls')),
    path('programlar/',include('programlar.urls')),
    path('account/',include('account.urls')),
    path('admin/', admin.site.urls),
]







