from django.forms import ModelForm
from .models import RiskDetail



class RiskDetailForm(ModelForm):
    class Meta:
        model = RiskDetail
        fields = '__all__'

