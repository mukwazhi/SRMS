from django.forms import ModelForm

from .models import  TrainingRecord
from django import forms


class RecordForm(ModelForm):
    class Meta:
        model = TrainingRecord
        fields = '__all__'


