from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def profile_index(request):
    return render(request, 'index.html')


def profile_book(request):
    return render(request, 'book.html')


def profile_customer(request):
    return render(request, 'customer.html')


def profile_cars(request):
    return render(request, 'cars.html')


def profile_return(request):
    return render(request, 'return.html')
