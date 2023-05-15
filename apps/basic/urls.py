from django.urls import path
from apps.basic.views import index
from .views import about_us

app_name = "basic"

urlpatterns = [
    path("", index, name="index"),
    path("about_us/", about_us, name="about_us"),
]
