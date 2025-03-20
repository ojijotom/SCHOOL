import json

from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from requests.auth import HTTPBasicAuth


from trainingapp.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def course_details(request):
    return render(request, 'course_details.html')

def courses(request):
    return render(request, 'courses.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def trainers(request):
    return render(request, 'trainers.html')

def starter_page(request):
    return render(request, 'starter_page.html')

def location(request):
    return render(request,'location.html')

#login $ register

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request,user)
            messages.success(request, "You are now logged in!")
            return redirect('/index')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')


def contact(request):
    if request.method == 'POST':
        mycontacts = Contacts(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],

        )
        mycontacts.save()
        return redirect('/show')

    else:
        return render(request, 'contact.html')


def show(request):
    all = Contacts.objects.all()
    return render(request,'show.html',{'all':all})



def edit_contact(request, id):
    appointment = get_object_or_404(Contacts, id=id)

    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.subject = request.POST.get("subject")
        appointment.message = request.POST.get("message")

        if 'image' in request.FILES:
            appointment.image = request.FILES['image']


        appointment.save()
        return redirect('show')  # Redirect to the page that lists all appointments

    return render(request, "edit.html", {"contact": contact})

def delete(request, id):
    myappointment = get_object_or_404(Contacts, id=id)

    if myappointment.image:
        myappointment.image.delete()  # Delete image file from storage

    myappointment.delete()
    return redirect('/show')


def admission(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        if image:  # Log file upload
            print(f"Uploaded File Name: {image.name}")
            print(f"File Size: {image.size} bytes")

            # Optional: Save to disk manually (debugging)
            path = default_storage.save(f"appointments/{image.name}", ContentFile(image.read()))
            print(f"File saved at: {path}")

        myadmission = Admission1(
             firstname=request.POST['firstname'],
             lastname=request.POST['lastname'],
            email=request.POST['email'],
            date=request.POST['date'],
            gender=request.POST['gender'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            image=image  # Assign image

        )
        myadmission.save()
        return redirect('/showstudents')

    else:
        return render(request, 'admission.html')


def showstudents(request):
    all1 = Admission1.objects.all()
    return render(request,'showstudents.html',{'all1':all1})


