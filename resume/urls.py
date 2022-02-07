from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkPageList.as_view(), name='about'),
]
