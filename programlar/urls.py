from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>', views.details, name="program_details"),
    path('kategori/<slug:slug>', views.getProgramlarByCategory, name='programlar_by_category')
]
