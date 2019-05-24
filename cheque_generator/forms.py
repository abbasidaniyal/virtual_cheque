from django.forms import ModelForm
from .models import Cheque


class ChequeForm(ModelForm):
    class Meta:
        model = Cheque
        fields = ['bearer', 'amount', 'issue_date']
