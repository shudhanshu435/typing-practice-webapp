from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import UserProfile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')

            # update email
            user.email = email
            user.save()

            # update full name of userprofile
            profile = UserProfile.objects.get(user=user)
            profile.full_name = full_name
            profile.save()

            return redirect('login')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'users/register.html', {'form':form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)

    return redirect('login')
