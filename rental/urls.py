from .views import RentalListCreateView, RentalRetrieveUpdateDeleteView
from django.urls import path
from . import views

urlpatterns = [
    path('rentals/', views.rental_list, name='rental_list'),
    path('rent/', views.rent_film, name='rent_film'),
    path('rentals/<int:rental_id>/edit/', views.rental_update, name='rental_update'),
    path('rentals/<int:pk>/delete/', views.rental_delete, name='rental_delete'),
    path('api/rentals/', RentalListCreateView.as_view(), name='rental-list-create'),
    path('api/rentals/<int:pk>/', RentalRetrieveUpdateDeleteView.as_view(), name='rental-detail'),
]
