from __future__ import unicode_literals

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django_daraja.views import stk_push_callback_url, cl

from .models import Student
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render






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
        amount = request.POST.get('amount')

        query = Student(name=name, email=email, age=age, gender=gender, country=country, city=city, amount=amount)
        query.save()
        return redirect("/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


# editing data views
def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')
        amount = request.POST.get('amount')


        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.gender = gender
        update_info.country = country
        update_info.city = city
        update_info.amount = amount
        update_info.save()

        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def pay(request, id):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'LA'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'index.html')