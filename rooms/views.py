from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Room

# Create your views here.
@login_required
def rooms(request):
    """this wil provide the rooms list"""
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {"rooms":rooms})


@login_required
def room(request, slug):
    """room detail view"""
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room = room)[0:25]


    return render(request, "rooms/room.html", {"room":room, "messages": messages})

