from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def cars(request):
    return render(request,'cars.html')
def food(request):
    return render(request,'food.html')