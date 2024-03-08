from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)


