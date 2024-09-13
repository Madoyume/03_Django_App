from django import forms

class HelloForm(forms.Form):
    check = forms.BooleanField(label='CheckBox', required=False)

class SessionForm(forms.Form):
    session = forms.CharField(label='session', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
