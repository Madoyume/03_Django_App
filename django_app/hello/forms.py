from django import forms
from .models import Friend, Message

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.EmailInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'birthday':forms.DateInput(attrs={'class':'form-control'}),
        }

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    str = forms.CharField(label='String', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "No"!')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content':forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':2}),
            'friend':forms.Select(attrs={'class':'form-control form-control-sm'}),
        }