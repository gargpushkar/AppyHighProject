from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('detail', views.FoodViewSet, basename = "FoodStore")

app_name = 'Food'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/<foodname>/', views.list, name='list'),
    path('detail/<foodname>/<int:pk>/', views.detail, name = 'detail'),
    path('add/', views.add_food, name='add_food'),
    path('add_m/', views.add_food_M, name='add_food_m'),
    path('api/', include(router.urls)),
]
