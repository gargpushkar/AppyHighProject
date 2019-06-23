from django.shortcuts import render, redirect
from .models import FoodStore
from .forms import FoodForm, AddFoodForm, AddFoodMForm
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):

    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            foodname = form.cleaned_data.get('name')
            return redirect('Food:list', foodname=foodname)
    else:
        form = FoodForm()
    return render(request, 'Food/home.html', {'form': form})


def list(request, foodname):
    obj = FoodStore.objects.filter(product_name__iexact=foodname)
    context = {
        'obj': obj,
        'foodname': foodname,
    }
    return render(request, 'Food/food_list.html', context=context)


def detail(request, foodname, pk):
    obj = FoodStore.objects.get(pk=pk)
    context = {
        'value' : obj.__dict__.items(),
        'foodname' : foodname
    }
    return render(request, 'Food/food_detail.html', context)

@login_required
def add_food(request):
    if request.method == "POST":
        form = AddFoodForm(request.POST)
        if form.is_valid():
            foodname = form.cleaned_data.get('product_name')
            form.save()
            return redirect('Food:list', foodname=foodname)
    else:
        form = AddFoodForm()
    return render(request,'Food/add_food.html',{'form':form})

@login_required
def add_food_M(request):
    if request.method == "POST":
        form = AddFoodMForm(request.POST)
        if form.is_valid():
            foodname = form.cleaned_data.get('product_name')
            form.save()
            return redirect('Food:list', foodname=foodname)
    else:
        form = AddFoodMForm()
    return render(request,'Food/add_food_m.html',{'form':form})

# restframework
from rest_framework import viewsets
from .serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        foodname = self.request.query_params.get('foodname')
        queryset = FoodStore.objects.filter(product_name__iexact=foodname)
        return queryset
