from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from account.models import jobSeeker
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    template_data = {}
    template_data['title'] = 'Applicants'
    template_data['applicants'] = jobSeeker.objects.all()

    if (not request.user.is_recruiter):
        return redirect('home.index')

    return render(request, 'applicants/index.html', {'template_data': template_data})