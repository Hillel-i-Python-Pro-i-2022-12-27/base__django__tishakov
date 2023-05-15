from django.urls import path
from apps.users.views import RegisterFormView, LoginFormView, logout, UserDetailView, UserUpdateView

app_name = "users"

urlpatterns = [
    path("registration/", RegisterFormView.as_view(), name="registration"),
    path("login/", LoginFormView.as_view(), name="login"),
    path("logout/", logout, name="logout"),
    path("profile/<int:pk>", UserDetailView.as_view(), name="profile"),
    path("update_profile/<int:pk>", UserUpdateView.as_view(), name="update_profile"),
]
