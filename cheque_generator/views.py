from django.shortcuts import render
from .forms import UserForm
from .models import Users
# Create your views here.
def create_user(request):
    form = UserForm(request.POST or none)
    if from.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "user/user_create.html",context)
    