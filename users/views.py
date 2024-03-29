from django.shortcuts import redirect, render

from . forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = UserRegisterForm()
    context = {
         'register_form': register_form
    }

    return render(request, 'users/register.html', context)


