from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [

    path('inbox/', views.inbox, name='inbox'),

    path('send/', views.send_message, name='send_message'),

    path('send/<int:user_id>/', views.send_message, name='send_user_message'),

]