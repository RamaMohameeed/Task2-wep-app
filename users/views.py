from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')

    users = User.objects.all()
    return render(request, 'users/user_list.html', {'form': form, 'users': users})

def toggle_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.status = not user.status
    user.save()
    return redirect('user_list')


# Create your views here.
