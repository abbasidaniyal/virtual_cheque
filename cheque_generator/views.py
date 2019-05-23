from django.shortcuts import render
from .forms import ChequeForm
from .models import Users
# Create your views here.


def create_user(request):
    form = ChequeForm(request.POST)
    if request.method =='POST':
        form=ChequeForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            'form': form
            }   
    else:
        form=ChequeForm()
        
    return render(request, "user/user_create.html",context)
    