from django.forms import ModelForm
from .models import Customer


class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"