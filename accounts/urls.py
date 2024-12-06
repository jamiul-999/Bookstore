from django.contrib.auth import views as auth_view
from django.urls import path

from .views import SignupPageView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout")
]