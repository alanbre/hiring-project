from django.shortcuts import render, redirect
from .models import Estados

def home(request):
    return render(request, 'home.html')

def postjob(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass
        else :
            return render(request, 'post_job.html', {'estados': Estados.objects.all()})
    else:
        return redirect('signin')

