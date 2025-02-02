from django.urls import path, include

from apps.jobs.views import job_detail, add_job, apply_for_job

urlpatterns = [
  path('add/', add_job, name='add_job'),
  path('<int:job_id>/', job_detail, name='job_detail'),
  path('<int:job_id>/apply/', apply_for_job, name='apply_for_job'),
]