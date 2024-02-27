from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("signup", views.UserViewSet)

urlpatterns = [
    path('login', views.login, name="login"),
    path('sign', views.signup, name="signup"),
]