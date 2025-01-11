from django import forms

from apps.jobs.models import Job

class AddJobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'short_description', 'long_description']