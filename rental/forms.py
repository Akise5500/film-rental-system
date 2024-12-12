from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'genre', 'synopsis', 'release_date', 'available']

from django import forms
from .models import Rental  # Ensure this import is present

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['return_date']
