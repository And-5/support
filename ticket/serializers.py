from rest_framework import serializers
from ticket.models import *
from django.contrib.auth.models import User


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['owner']


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        exclude = ['ticket', 'id']


class MessageListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ['id', 'owner', 'ticket', 'text', 'created']


class MessageDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ['owner', 'ticket', 'text', 'created', 'ticket']


class TicketListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['status']


class TicketDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    messages = MessageSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'owner', 'title', 'description', 'status', 'created', 'messages']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserDetailSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tickets']

