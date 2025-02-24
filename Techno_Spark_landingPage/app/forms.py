from django import forms


class leadForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.IntegerField()
    email = forms.CharField(max_length=100)
    

