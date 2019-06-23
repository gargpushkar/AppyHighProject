from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', user_views.UserViewSet, basename = "User")

app_name = 'users'
urlpatterns = [
    # path('', include(router.urls)),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
]