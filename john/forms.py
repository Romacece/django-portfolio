# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # Définir les widgets avec les placeholders et les valeurs par défaut
            self.fields['name'].widget.attrs.update({
                'class': 'contact__input',
                'placeholder': 'Name ',  # Utiliser le libellé du champ comme placeholder
                'value': self.fields['name'].label,  # Pré-remplir avec le libellé du champ
            })

            self.fields['email'].widget.attrs.update({
                'class': 'contact__input',
                'placeholder': 'Email',
                'value': self.fields['email'].label,
            })

            self.fields['message'].widget.attrs.update({
                'class': 'contact__input',
                'placeholder': 'Message',
                'value': self.fields['message'].label,
            })
        