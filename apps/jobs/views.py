from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.jobs.forms import AddJobForm, ApplicationForm
from apps.jobs.models import Job

def job_detail(request, job_id):
  job = Job.objects.get(pk=job_id)

  return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
  job = Job.objects.get(pk=job_id)

  if request.method == 'POST':
    form = ApplicationForm(request.POST)

    if form.is_valid():
      application = form.save(commit=False)
      application.job = job
      application.created_by = request.user
      application.save()

      return redirect('dashboard')
    else:
      form = ApplicationForm()
      
    return render(request, 'jobs/apply_for_job.html', {'job': job, 'form': form})

@login_required
def add_job(request):
  if request.method == 'POST':
    form = AddJobForm(request.POST)

    if form.is_valid():
      job = form.save(commit=False)
      job.created_by = request.user
      job.save()

      return redirect('dashboard')
  else:
    form = AddJobForm()

  return render(request, 'jobs/add_job.html', {'form': form})