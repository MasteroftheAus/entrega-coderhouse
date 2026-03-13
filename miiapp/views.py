from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, ListView, CreateView, UpdateView
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from .models import user, post, Avatar
from .forms import PostForm, userForm, AvatarForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request, "miiapp\index.html")

def home(request):
    context = {"mmensaje": "This is the Main Page"}
    return render(request, "miiapp\home.html", context)



class UserListView(ListView):
    model = user
    template_name = 'miiapp/users_list.html'
    context_object_name = 'user'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = post
    form_class = PostForm
    success_url = reverse_lazy("miiapp/post_lists.html")


class UserDetailView(DetailView):
    model = user
    template_name = 'miiapp/users_detail.html'
    context_object_name = 'user'

class UserUpdateView(UpdateView):
    model = user
    fields = ['name', 'surname', 'email']
    template_name = 'miiapp/user_form.html'
    success_url = '/users_list/'

class UserDeleteView(DeleteView):
    model = user
    template_name = 'miiapp/user_confirm_delete.html'
    success_url = '/users/'


def about(request):
    return render(request, "miiapp/about.html")

def create_user(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = userForm()
    return render(request, 'miiapp/create_users.html', {'form': form})

def CathegoryCreate(request):
    if request.method == "GET":
        form = forms.CathegoryForm()
    if request.method == "POST":
        form = forms.CathegoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("miiapp.post_lists")
    return render(request, 'miiapp/cathegory_create.html', context= {"form": form})


@login_required
def profile(request):
    return render(request, 'miiapp/profile.html')

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar=None

        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect('miiapp:profile')
    else:
        form = UserChangeForm(instance=request.user)
        if hasattr(request.user, "avatar"):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request,'miiapp/edit_profile.html',{'form': form, 'avatar_form': avatar_form}
)





@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.avatar)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=request.user.avatar)
    return render(request, 'upload_avatar.html', {'form': form})

class PostListView(ListView):
    model = post
    template_name = "miiapp/post_lists.html"
    context_object_name = "posts"

    def get_queryset(self):
        search  = self.request.GET.get("search", None)
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    form_class = PostForm
    success_url = reverse_lazy("miiapp:post_lists")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            form.add_error(None,"User must be logged in to create a post.")
            return self.form_invalid(form)
        return super().form_valid(form)
    

class PostDetailView(DetailView):
    model = post
    template_name = "miiapp/post_details.html"

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = post
    success_url= reverse_lazy("miiapp:post_lists")


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "miiapp:sign_up.html"
    success_url = reverse_lazy("login")
    success_message = "Your profile was created without a hitch!"


@login_required
def inbox(request):

    messages = Message.objects.filter(receiver=request.user)

    return render(request, 'messaging/inbox.html', {'messages': messages})




#def confirm_delete(request, pk: int):
#    post = post.objects.get(id=pk)
#    context = {"id": id}
#    return render(request, 'miiapp/post_detail.html', context)

#def update_user(request, pk):
#    user = get_object_or_404(user, pk=pk)
#    if request.method == 'POST':
#        form = userForm(request.POST, instance=user)
#        if form.is_valid():
#            form.save()
#            return redirect('user_list')
#    else:
#        form = userForm(instance=user)
#    return render(request, 'miiapp/update_user.html', {'form': form})

# def delete_user(request, pk):
#    user = get_object_or_404(user, pk=pk)
#    user.delete()
#    return redirect('user_list')

# def users_detail(request, pk):
#    user = get_object_or_404(user, pk=pk)
#    return render(request, 'miiapp/users_detail.html', {'user': user})

#def post_list(request):
    #search = request.GET.get("search", None)
    #if search:
    #    post_list = post.objects.filter(title__icontains=search)
    #else:
     #   post_list = post.objects.all()
    # return render(request, "miiapp/post_lists.html", context= {"posts": post_list})

#def post_details(request, pk: int):
 #   post = post.objects.get(id=pk)
  #  context = {"id": id}
   # return render(request, 'miiapp/post_detail.html', context)

# def cathegory_details(request, pk: int):
    #request.GET.get("search")
    #if search:
        #cathegory = models.cathegory.objects.filter(name__contains=search)
    #else:
        #cathegory = models.cathegory.objects.all()


#def post_create(request):
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            if request.user.is_authenticated:
#                post.author = request.user
#                post.save()
#                return redirect("miiapp/post_lists.html")
#            else:
#                form.add_error(None,"User must be logged in to create a post.")
#    else:
#        form = PostForm()
#    return render(request, 'miiapp/post_create.html', context={"form": form})