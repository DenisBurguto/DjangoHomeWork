
from django import forms

from htapp2.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

# class ProductForm2(forms.Form):
#     name = forms.CharField(max_length=50,
#                            widget=forms.TextInput(attrs={'class': 'form-control',
#                                                          'placeholder': 'new product name'}))
#
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
#                                                             'placeholder': 'user@mail.ru'}))
#     age = forms.IntegerField(min_value=18,
#                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     is_active = forms.BooleanField(required=False,
#                                    widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     birthdate = forms.DateField(initial=datetime.date.today,
#                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F',
#                                                         'Female')],
#                                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
