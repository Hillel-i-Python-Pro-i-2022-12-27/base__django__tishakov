from django.shortcuts import render


def index(request):
    context = {
        "title": "Home Page",
    }

    return render(
        request=request,
        template_name="index.html",
        context=context,
    )
