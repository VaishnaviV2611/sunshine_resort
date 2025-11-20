from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'bookingapp/home1.html')

def login_view(request):
    return render(request,'bookingapp/login1.html')

def book_view(request):
    return render(request,'bookingapp/book1.html')