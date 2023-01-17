from django import forms


class LeaveRequestForm(forms.Form):
    Name = forms.CharField(label="Имя")
    PhoneNumber = forms.CharField(label="Номер телефона")
    Email = forms.EmailField(label="E-mail")
