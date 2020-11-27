from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
import random
from .forms import VisitorForm
from .models import User
from .models import Client, Visitor
from .models import Appointment
# Create your views here.

def index(request):
    return render(request, "appointment/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "appointment/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "appointment/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "appointment/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "appointment/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "appointment/register.html")
def appointment(request):
    if request.method == 'POST':  # data sent by user
        form = VisitorForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            subject= request.POST["subject"]
            phone=request.POST["phone"]
            appointId=random.randrange(1000,9000)
            d=Client()
            d.appointmentID= appointId
            d.name= name
            d.email= email
            d.subject= subject
            d.phone= phone
            d.save()
            form.save()  # this will save Car info to database
            msg = f'{name} your appointment ID is {appointId}, please memorize it'
            return render(request, "appointment/print.html", {'message': msg})
    else:  # display empty form
        form = VisitorForm()


    return render(request, "appointment/appointment.html", {'visitor_form': form})
def print(request, msg):
    return render(request, "appointment/print.html", {'message': msg})
def viewAppointment(request):
    if request.method == "POST":
        apId=request.POST["ID"]
        try:
            client=Client.objects.get(appointmentID=apId)
        except Client.DoesNotExist:
            msg=f'Appointment does not exist'
            return render(request, "appointment/print.html", {'message': msg})
        user= Visitor.objects.get(phone=client.phone)
        msg = f'Name:{user.name} \n Phone Number: {user.phone} \n Email Adress: {user.email} \n Subject: {user.subject} \n Date: {user.day}   Hour: {user.hour}'
        return render(request, "appointment/print.html", {'message': msg})
    else:
        return render(request, "appointment/view.html")
def deleteAppointment(request):
    if request.method == "POST":
        apId=request.POST["ID"]
        try:
            client=Client.objects.get(appointmentID=apId)
        except Client.DoesNotExist:
            msg=f'Appointment does not exist'
            return render(request, "appointment/print.html", {'message': msg})
        user= Visitor.objects.get(phone=client.phone)
        msg = f'Name:{user.name} your appointment was deleted'
        user.delete()
        client.delete()
        return render(request, "appointment/print.html", {'message': msg})
    else:
        return render(request, "appointment/delete.html")
def editAppointment(request):
    if request.method == "POST" and 'name' not in request.POST:
        apId=request.POST["ID"]
        try:
            client=Client.objects.get(appointmentID=apId)
        except Client.DoesNotExist:
            msg=f'Appointment does not exist'
            return render(request, "appointment/print.html", {'message': msg})
        user= Visitor.objects.get(phone=client.phone)
        return render(request, "appointment/edit.html", {'client': user})
    elif request.method == "POST" and 'name' in request.POST:
        users= Visitor.objects.all()
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject= request.POST.get("subject")
        phone=request.POST.get("phone")
        user= users.get(phone=phone)
        user.phone= phone
        user.name=name
        if email is not None:
            user.email=email
        user.subject=subject
        user.save()
        client =Client.objects.get(phone=user.phone)
        msg = f'Appointment ID: {client.appointmentID} Name:{user.name} \n Phone Number: {user.phone} \n Email Adress: {user.email} \n Subject:{user.subject} \n Date: {user.day}'
        return render(request, "appointment/print.html", {'message': msg})
    else:
        return render(request, "appointment/edit.html")

def showList(request):
    return render(request, "appointment/show.html", {
        # this will fetch all cars from database
        'users': Visitor.objects.all()
    })