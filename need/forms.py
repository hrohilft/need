from django import forms

from .models import Need, Transl

class NeedForm(forms.ModelForm):

    class Meta:
        model = Need
        fields = ('what', 'amount', 'where')

class TranslForm(forms.ModelForm):

    class Meta:
        model = Transl
        fields = ('text',)
