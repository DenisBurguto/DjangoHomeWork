from django.shortcuts import render


def main(request):
    return render(request, "htapp3/main.html")


def about(request):
    return render(request, "htapp3/about.html")

# Create your views here.
