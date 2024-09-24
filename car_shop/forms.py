from django import forms
from .models import Car, CommentCar


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class CommentFrom(forms.ModelForm):
    class Meta:
        model = CommentCar
        fields = "__all__"
