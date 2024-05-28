from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Vehicle, Chalan
from .forms import VehicleForm, ChalanForm
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vehicle_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register_user.html', {'form': form})

def add_chalan(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        form = ChalanForm(request.POST)
        if form.is_valid():
            chalan = form.save(commit=False)
            chalan.vehicle = vehicle
            chalan.save()  
            return redirect('vehicle_list')  
    else:
        form = ChalanForm()
    return render(request, 'add_chalan.html', {'form': form, 'vehicle': vehicle})


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    vehicle_data = []

    for vehicle in vehicles:
        total_chalans = Chalan.objects.filter(vehicle=vehicle).count()
        total_amount = Chalan.objects.filter(vehicle=vehicle).aggregate(total=Sum('amount'))['total'] or 0
        vehicle_data.append({
            'vehicle': vehicle,
            'total_chalans': total_chalans,
            'total_amount': total_amount
        })
    return render(request, 'vehicle_list.html', {'vehicle_data': vehicle_data})

def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('vehicle_list') 
    else:
        form = VehicleForm()
    return render(request, 'register_vehicle.html', {'form': form})

def chalan_list(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    chalans = Chalan.objects.filter(vehicle=vehicle)
    return render(request, 'chalan_list.html', {'vehicle': vehicle, 'chalans': chalans})


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicle.delete()
    return HttpResponseRedirect(reverse('vehicle_list'))