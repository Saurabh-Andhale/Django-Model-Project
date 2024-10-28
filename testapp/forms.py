
from django import forms
from testapp.models import student

class studentForm(forms.ModelForm):
    name=forms.CharField()
    mark=forms.IntegerField()
    class Meta:
        model=student
        fields='__all__'