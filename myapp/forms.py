from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)


class ProductForm(forms.Form):
    id = forms.IntegerField(min_value=1)
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    image = forms.ImageField(required=False, widget=forms.FileInput)
