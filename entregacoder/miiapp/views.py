from django.shortcuts import render

def index(request):
    context = {"Mensaje": "Bienvenidos a esta app"}
    return render(request, "miiapp\index.html", context)

def home(request):
    context = {"mmensaje": "Esta es la Home"}
    return render(request, "miiapp\home.html", context)

# Create your views here.


from django.shortcuts import render, get_object_or_404
from .models import user

def users_list(request):
    users = user.objects.all()
    return render(request, 'miiapp/users_lists.html', {'usuarios': users})

def users_detail(request, pk):
    user = get_object_or_404(user, pk=pk)
    return render(request, 'miiapp/users_detail.html', {'user': user})