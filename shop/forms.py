from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(attrs={'id': 'id_rating_hidden'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'maxlength': '500',
                'placeholder': 'Escribe tu opinión (máx. 500 caracteres)...'
            }),
        }
