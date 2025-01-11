from django.urls import path, include

from apps.userprofile.views import dashboard

urlpatterns = [
  path('', dashboard, name='dashboard'),
]