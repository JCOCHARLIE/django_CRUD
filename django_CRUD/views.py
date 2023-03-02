from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student


def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def edit(request):
    return render(request, "edit.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        query = Student(name=name, email=email, age=age, gender=gender, country=country, city=city)
        query.save()
        return redirect("/")

        return render(request, 'index.html')

def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")