from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from .models import job

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Jobs'
    template_data['jobs'] = job.objects.all()
    return render(request, 'jobs/index.html', {'template_data': template_data})

def apply(request, id):
    job_instance = get_object_or_404(job, id=id)

    context = {
        'job': job_instance,
    }

    return render(request, 'jobs/applied.html', context)

def edit(request, id):
    job_instance = get_object_or_404(job, id=id)
    if job_instance.company != request.user.recruiter_profile.company_name:
        return redirect('jobs.index')
    
    if request.method == "POST":

        pass

    return render(request, 'jobs/edit.html', {'job': job_instance})