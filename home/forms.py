from .models import Contact,Career
from django.forms import ModelForm,TextInput,EmailInput ,Textarea


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets={
            'name': TextInput(attrs={
                'class': "form-control input-wrap input-wrap-2 input-cols",
                'style': 'max-width: 800px;',
                'placeholder': ''
                }),
            'email': EmailInput(attrs={
                'class': "form-control input-wrap", 
                'style': 'max-width: 800px;',
                'placeholder': ''
                }),
            'subject': TextInput(attrs={
                'class': "form-control input-wrap input-wrap-2 input-cols",
                'style': 'max-width: 800px;',
                'placeholder': ''
                }),
            'message': Textarea(attrs={'cols':25, 'rows': 10}),
            
        }

class CareerForm(ModelForm):

    class Meta:
        model = Career
        fields = ['name','email','message']
        widgets={
            'name': TextInput(attrs={
                'class': "form-control input-wrap",
                'style': 'max-width: 800px; background:none;',
                'placeholder': ''
                }),
            'email': EmailInput(attrs={
                'class': "form-control input-wrap", 
                'style': 'max-width: 800px; background:none;',
                'placeholder': ''
                }),
            'message': Textarea(attrs={'cols':25, 'rows': 5,
                        'class': "form-control input-wrap",
                        'style': "background:none; border-style: solid; border-color:-internal-light-dark(rgb(118, 118, 118), rgb(133, 133, 133)); border-width: 2px;",
                        'placeholder': "Why You?"
            }),
            
        }