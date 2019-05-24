from django.shortcuts import render,redirect
from .forms import ChequeForm
from .models import Users
from static.cheque_maker.cheque_script import generate_cheque
# Create your views here.


def create_user(request):
    form = ChequeForm(request.POST)
    if request.method =='POST':
        form=ChequeForm(request.POST)
        if form.is_valid():

            form.save()
            bearer_name=form.cleaned_data.get('bearer')
            issue_date=form.cleaned_data.get('issue_date')
            amount=form.cleaned_data.get('amount')
            
            generate_cheque("temp",amount,issue_date,bearer_name)
            return redirect(f'static/cheque_maker/outputs/temp.jpg')
            
    else:
        form=ChequeForm()
        
    return render(request, "users/user_create.html",{'form':form})
    