import os
from uuid import uuid4
import json

from django.core.paginator import Paginator

from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import UserProfile, Employee, Netflix, Planet
from django.core.files.storage import FileSystemStorage
from app.forms import UserCreateForm, EmployeeForm
from app.script_xls import bulkcreate_netflix
from app.tasks import send_email_with_template_attachment
# Create your views here.


@login_required
def home(request):
    context = {'username': request.user.username}
    return render(request, 'home.html', context=context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # save user profile
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            user_profile = UserProfile.objects.create(user=user)

            # generate token and save
            token = uuid4().hex
            user_profile.token = token
            user_profile.save()

            # send email
            verify_url = "http://localhost:8000/verify_email?token={}&email={}".format(
                token, email
            )
            body = """
            Hello {},

            Please verify your email by click the following link
            {}
            """.format(user.username, verify_url)

            send_mail(
                'Please verify your email',
                body,
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreateForm()
        return render(request, 'signup.html', {'form': form})


def verify_email(request):
    email = request.GET['email']
    token = request.GET['token']

    user = User.objects.filter(email=email).first()

    if user is None:
        return HttpResponse("Invalid Email")

    up = UserProfile.objects.get(user=user)
    if up.token == token:
        up.is_verified = True
        up.save()
        return redirect('home')
    else:
        return HttpResponse("Invalid Token")


def login(request):

    if request.user.is_authenticated:
        return render(request, 'home')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        if user is None:
            return HttpResponse("Invalid username")

        up = UserProfile.objects.get(user=user)
        if up.is_verified == False:
            return HttpResponse("Please verify your email before login")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form})


@login_required
def get_user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {"user": user})


def employee_home(request):
    employees = Employee.objects.all()

    return render(request, 'home_employee.html', {"employees": employees})


def employee_new(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            send_email_with_template_attachment.delay(email)
        return redirect('employee_home')
    else:
        form = EmployeeForm()
        return render(request, 'add_employee.html', {"form": form})


def employee_edit(request):
    employee_id = request.GET['id']
    employee = Employee.objects.filter(id=employee_id).first()
    if employee is None:
        return HttpResponse("Please enter valid data")
    emp_dict = {'name': employee.name, 'email': employee.email}

    form = EmployeeForm(emp_dict)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_home')

    return render(request, 'edit.html', {"form": form})


def netflix_list(request):
    return render(request, 'netflix_list.html')


def netflix(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']

        fs = FileSystemStorage()
        filename = fs.save(upload_file.name, upload_file)
        filepath = os.path.join(fs.location, filename)
        bulkcreate_netflix(filepath)
        return redirect('/netflix_list')
    return render(request, 'netflix.html')


def netflix_paginate_data(request):

    start = int(request.GET['start'])
    length = int(request.GET['length'])
    page_no = int((start + length)/length)

    netflix = Netflix.objects.all()
    p = Paginator(netflix, length)
    page_display = p.page(page_no)
    data = list(page_display.object_list.values())

    context = {
        "draw": request.GET['draw'],
        "data": data,
        "recordsTotal": len(netflix),
        "recordsFiltered": len(netflix),
    }
    return JsonResponse(context, safe=False)


def netflix_paginate(request):
    netflix = Netflix.objects.all()
    no_of_rows = 100
    p = Paginator(netflix, no_of_rows)
    no_of_pages = list(range(1, p.num_pages+1))
    context = {
        "no_of_pages": no_of_pages,
    }

    return render(request, 'netflix_paginate.html', context=context)


def netflix_data(request):
    netflix = list(Netflix.objects.all().values())

    return JsonResponse(netflix, safe=False)


def planet_paginate(request):
    planet = Planet.objects.all()
    no_of_rows = 1000
    p = Paginator(planet, no_of_rows)
    no_of_pages = list(range(1, p.num_pages+1))
    context = {
        "no_of_pages": no_of_pages,
    }

    return render(request, 'planet_paginate.html', context=context)


def planet_paginate_data(request):
    start = int(request.GET['start'])
    length = int(request.GET['length'])
    page_no = int((start + length)/length)

    planet = Planet.objects.all()
    p = Paginator(planet, length)
    page_display = p.page(page_no)
    data = list(page_display.object_list.values())

    context = {
        "draw": request.GET['draw'],
        "data": data,
        "recordsTotal": len(planet),
        "recordsFiltered": len(planet),
    }
    return JsonResponse(context, safe=False)


def planet_data(request):
    planet = list(Planet.objects.all().values())

    return JsonResponse(planet, safe=False)


def planet_data_dispaly(request):
    return render(request, 'planet_data_display.html')
