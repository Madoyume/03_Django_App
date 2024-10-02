from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    requeired = forms.IntegerField(label='Requeired', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    min = forms.IntegerField(label='Min', min_value=100, \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    max = forms.IntegerField(label='Max', max_value=1000, \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    date = forms.DateField(label="Date", input_formats=['%d'], \
        widget=forms.DateInput(attrs={'class':'form-control'}))
    time = forms.TimeField(label='Time', \
        widget=forms.TimeInput(attrs={'class':'form-control'}))