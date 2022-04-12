from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        # context = {"count":"Hello World"}
        return render(request, "counter/index.html")


class Room(View):
    def get(self, request, room_name):
        return render(request, "counter/room.html", {"room_name":room_name})