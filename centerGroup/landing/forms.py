from django import forms


class LeaveRequestForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    PhoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телфона'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
