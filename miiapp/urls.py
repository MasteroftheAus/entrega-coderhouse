from django.contrib import admin
from django.urls import path
from miiapp import views
from .views import UserListView
from miiapp.views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
app_name = "miiapp"


urlpatterns = [
    path("", views.index, name= "index"),
    path('post_lists', views.PostListView.as_view(), name = 'post_lists'),
    path('home/', views.home, name= "home"),
    #path('create/users/', views.users_list, name="make"),
    path('users_list/', UserListView.as_view(), name="users_list_view"),
    path('user_detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('update_users/<int:pk>', views.UserUpdateView.as_view(), name="update_users"),
    path('delete_users/<int:pk>', views.UserDeleteView.as_view(), name="delete_users"),
    path('type_create/', views.CathegoryCreate, name='type_create'),
    path('post_form/', views.PostCreateView.as_view(), name= 'post_form'),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(), name= 'post_update'),
    path('post_details/<int:pk>', views.PostDetailView.as_view(), name= 'post_details'),
    path('post_confirm_delete/<int:pk>', views.PostDeleteView.as_view(), name= 'post_confirm_delete'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("about/", views.about, name="about"),
    


]
