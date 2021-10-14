from django import forms
from .models import CSVs

class CSVsModelForm(forms.ModelForm):
    class Meta:
        model = CSVs
        fields = ('file_name',)

