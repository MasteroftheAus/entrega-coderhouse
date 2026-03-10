from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import user




# Create your views here.

def index(request):
    return render(request, "miiapp\index.html")

def home(request):
    context = {"mmensaje": "This is the Main Page"}
    return render(request, "miiapp\home.html", context)

def post_list(request):
    post_list = Post.objects.all()
    return render(request, "/post_lists.html", context={"posts" = posts_lists})


def users_list(request):
    users = user.objects.all()
    return render(request, 'miiapp/users_lists.html', {'usuarios': users})

def users_detail(request, pk):
    user = get_object_or_404(user, pk=pk)
    return render(request, 'miiapp/users_detail.html', {'user': user})
