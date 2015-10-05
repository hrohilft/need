from django import forms

from .models import Need

class NeedForm(forms.ModelForm):

    class Meta:
        model = Need
        fields = ('what', 'amount', 'where')


