from django.shortcuts import render


# Vista para Home
def home(request):
    return render(request, "home.html")


# Vista para About
def about(request):
    return render(request, "about.html")


# Vista para Contact (con un mini formulario)
def contact(request):
    return render(request, "contact.html")
