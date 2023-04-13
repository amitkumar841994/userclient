from django import forms
from .models import Food

class foodform(forms.ModelForm):
    class Meta:
        model=Food
        fields =['food_image']