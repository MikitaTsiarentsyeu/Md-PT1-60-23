from .models import Regi

from django.forms import ModelForm, TextInput, Textarea
class RegiForm(ModelForm):
    class Meta:
        model = Regi
        fields = ['name','mail','phone', 'details']

        widgets = {
            "name":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ваше имя'
            }),
             "mail":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'e-mail'
            }),
             "phone":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ваш телефон'
            }),
             "details":Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Детали заказа'
            })
        }