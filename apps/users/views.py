from django.contrib import auth
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect, redirect
from django.views.generic import DetailView, FormView, UpdateView
from apps.users.forms import RegisterUserForm
from django.urls import reverse, reverse_lazy

User = get_user_model()


class RegisterFormView(FormView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("root:home_page")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("basic:index")


class LoginFormView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("basic:index"))


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "photo",
    )

    success_url = reverse_lazy("basic:index")
