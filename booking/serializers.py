from rest_framework import serializers
from booking.models import user , book_ticket , ticket

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('user_id', 'name', 'email')


class book_ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = book_ticket
        fields = ('user_id','ticket_id')

class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = ('ticket_id','seat_id','aircomp','flight_number','price','destination','booked')
