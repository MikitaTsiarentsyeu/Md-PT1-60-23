from .models import Base
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.core.exceptions import ValidationError


class RegiForm(ModelForm):
  
    class Meta:
        model = Base
        
        fields = ['name', 'autor']

        widgets = {
            "name":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Книга'
            }),
            
             "autor":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Автор'
            }),
             
            
           
        }

    def clean_subtitle(self):
        name_data = self.cleaned_data['name']
        autor_data =self.cleaned_data['autor']

        

                

        return True

    


# class Add(forms.Form):

#     name = forms.CharField(label="Title", max_length = 50)
#     mail = forms.CharField(max_length = 50)
#     phone = forms.CharField( max_length = 50)
#     details = forms.CharField(widget=forms.Textarea(attrs={'class':'text'}))
  
#     def clean_subtitle(self):
#         name_data = self.cleaned_data['name']
#         mail_data = self.cleaned_data['mail']
        

#         if name_data == mail_data:
#             raise ValidationError("Name or mail is similar")

#         return mail_data