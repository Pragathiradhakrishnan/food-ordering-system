from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name','phone','address']
        widgets = {
            'customer_name':forms.TelInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'phone':forms.TelInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Delivery Address','rows':4}),
        }