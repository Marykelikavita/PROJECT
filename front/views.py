from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(request, 'front/landing_page.html')


@login_required(login_url='login')
def index(request):
    return render(request, 'front/index.html')


@login_required(login_url='login')
def results_page(request):
    return render(request, 'predictions/prediction_result.html')
    


@login_required(login_url='login')
def visualizations(request):
    return render(request, 'predictions/visualizations.html')