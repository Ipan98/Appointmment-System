from django.forms import ModelForm
from .models import Visitor

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        exclude = ()  # this says to include all fields from model to the form

