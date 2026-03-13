from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageForm

def inbox(request):

    messages = Message.objects.filter(receiver=request.user)

    return render(request, 'messaging/inbox.html', {'messages': messages})


@login_required
def send_message(request, user_id=None):

    receiver = None

    if user_id:
        receiver = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')

    else:
        if receiver:
            form = MessageForm(initial={'receiver': receiver})
        else:
            form = MessageForm()

    return render(request, 'messaging/send_message.html', {'form': form})