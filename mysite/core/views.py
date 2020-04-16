from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
def home(request):
    count = User.objects.count()
    return render(request,'home.html',{
    	'count':count
    }
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
    	form = UserCreationForm()
    return render(request, 'registration/signup.html',
    	{
        'form': form
    })
#if we dont use the login_required the user can access the secret page without autentication.
@login_required
def temp_convert(request):
    return render(request, 'temp_convert.html')

#another method for the above!
@login_required
def calculator(request):
    return render(request, 'calculator.html')


@login_required
def password(request):
    return render(request, 'password.html')

@login_required
def count(request):
    return render(request, 'count.html')


@login_required
def guess(request):
    return render(request, 'guess.html')