from django.shortcuts import render, get_object_or_404, redirect
from .models import Rental, Film
from .forms import RentalForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# View to list all rentals by the logged-in customer
@login_required
def rental_list(request):
    rentals = Rental.objects.filter(customer=request.user)
    return render(request, 'rental/rental_list.html', {'rentals': rentals})

# View to create a new rental (rent a film)
@login_required
def rent_film(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.customer = request.user
            rental.save()
            return redirect('rental_list')
    else:
        form = RentalForm()
    return render(request, 'rental/rent_film.html', {'form': form})

# View to update rental details
@login_required
def rent_film(request):
    films = Film.objects.all()
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.customer = request.user
            rental.film_id = request.POST.get('film')
            rental.save()
            return redirect('rental_list')
    else:
        form = RentalForm()
    return render(request, 'rental/rent_film.html', {'form': form, 'films': films})

# View to cancel a rental
@login_required
def rental_delete(request, pk):
    rental = get_object_or_404(Rental, pk=pk, customer=request.user)
    if request.method == 'POST':
        rental.delete()
        return redirect('rental_list')
    return render(request, 'rental/rental_confirm_delete.html', {'rental': rental})

@login_required
def rental_update(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    if request.method == 'POST':
        form = RentalForm(request.POST, instance=rental)
        if form.is_valid():
            form.save()
            return redirect('rental_list')
    else:
        form = RentalForm(instance=rental)
    return render(request, 'rental/rental_update.html', {'form': form, 'rental': rental})

# rental/views.py
from rest_framework import generics
from .models import Rental
from .serializers import RentalSerializer

# List all rentals or create a new rental (Read and Create)
class RentalListCreateView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

# Retrieve, update, or delete a rental (Read, Update, Delete)
class RentalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
