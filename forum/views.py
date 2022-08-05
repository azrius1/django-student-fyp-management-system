from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
import sqlite3
from django.views.generic import TemplateView


# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html')

def room(request, room):
    room_details = Room.objects.get(name=room)
    username = request.user.username
    return render(request, 'forum/room.html', {
        'forum_username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.user.username

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username+'/')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username+'/')

def send(request):
    message = request.POST['message']
    username = request.user.username
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def catalog (request):
    details = Room.objects.all()
    return render(request, 'forum/forum.html', {'detail':details})

# def getRoomList():
#     connection = sqlite3.connect('sqlite3.db')
#     cursor = connection.cursor()
#     print("List of available rooms:")

#     sqlite3_select_query = """SELECT * from chat_room"""
#     cursor.execute(sqlite3_select_query)
#     records = cursor.fetchall()
#     print ("Total rooms are: ", len(records))
#     print("Printing each row")
#     for row in records:
#         print("Id:", row[0])
#         print("Name:", row[1])
#         print("\n")
    
#     cursor.close()
#     connection.close()