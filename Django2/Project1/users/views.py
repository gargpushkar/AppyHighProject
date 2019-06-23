from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# restframework
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        queryset = User.objects.filter(username = user)
        return queryset


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to login.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
