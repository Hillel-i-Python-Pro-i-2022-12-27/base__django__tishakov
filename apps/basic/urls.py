from django.urls import path
from apps.basic.views import index

app_name = "basic"

urlpatterns = [
    path("", index, name="index"),
]
