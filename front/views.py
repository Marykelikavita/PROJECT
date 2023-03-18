from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import DataForm
# Create your views here.

def landing_page(request):
    return render(request, 'front/landing_page.html')


@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'predictions/prediction_result.html')
    else:
        form = DataForm()
    context = {
        'form': form
    }
    return render(request, 'front/index.html', context)


@login_required(login_url='login')
def results_page(request):
    return render(request, 'predictions/prediction_result.html')
    


@login_required(login_url='login')
def visualizations(request):
    return render(request, 'predictions/visualizations.html')