from django.forms import ModelForm 
from .models import Cheque

class ChequeForm(ModelForm):
    class Meta:
        model = Cheque
        fields = ['issuer','issue_date','amount']
        