from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name', 
            'class': 'form-control'
        })
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your age',  # Corrected the typo here
            'class': 'form-control'
        })
    )