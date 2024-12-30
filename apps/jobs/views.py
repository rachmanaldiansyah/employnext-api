from django.shortcuts import render

from apps.jobs.models import Job

def job_detail(request, job_id):
  job = Job.objects.get(pk=job_id)

  return render(request, 'jobs/job_detail.html', {'job': job})