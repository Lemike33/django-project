from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkPage.as_view(), name='about'),
]
