from booking.models import user , book_ticket , ticket
from booking.serializers import userSerializer, book_ticketSerializer , ticketSerializer
from rest_framework import generics
#import random

class userList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer

class userRandomfind(generics.ListCreateAPIView):
    #queryset = random.choice(user.objects.all())
    queryset = user.objects.all().order_by('?')[:1]
    serializer_class = userSerializer

class findUser(generics.ListCreateAPIView):
    serializer_class = userSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = user.objects.all()
        username = self.request.query_params.get('name', None)
        if username is not None:
            queryset = queryset.filter(name=username)
        return queryset

class findTicket(generics.ListCreateAPIView):
    serializer_class = ticketSerializer
    def get_queryset(self):
        queryset = ticket.objects.all()
        price = self.request.query_params.get('price', None)
	destination = self.request.query_params.get('dest',None)
	available = self.request.query_params.get('avail', None)
        queryset = queryset.filter( price__lte = price , booked = available , destination = destination )[:1]
        return queryset

class UpdateTicket(generics.UpdateAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()

class bookTicket(generics.ListCreateAPIView):
    queryset = book_ticket.objects.all()
    serializer_class = book_ticketSerializer

