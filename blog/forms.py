from django import forms

from blog.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    rating = forms.FloatField()
    discount = forms.IntegerField()
    quantity = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'rating', 'discount', 'quantity']
        exclude = ()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'rating', 'discount', 'quantity']
        exclude = ()
