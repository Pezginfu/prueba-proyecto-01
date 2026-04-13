from django import forms
from django.core.validators import RegexValidator
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', message="Solo se permiten letras.")],
        widget=forms.TextInput(attrs={'maxlength': '15', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', message="Solo se permiten letras.")],
        widget=forms.TextInput(attrs={'maxlength': '15', 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={'maxlength': '30', 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\+?[0-9]+$', message="Solo se permiten números.")],
        widget=forms.TextInput(attrs={'maxlength': '12', 'class': 'form-control'})
    )
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'maxlength': '30', 'class': 'form-control'})
    )
    postal_code = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^[0-9]+$', message="Solo se permiten números.")],
        widget=forms.TextInput(attrs={'maxlength': '10', 'class': 'form-control'})
    )
    city = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'maxlength': '15', 'class': 'form-control'})
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address',
                  'postal_code', 'city']
