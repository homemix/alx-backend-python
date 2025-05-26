from rest_framework import serializers
from rest_framework.serializers import CharField, SerializerMethodField, ValidationError

from .models import Conversation, Message, User


class UserSerializer(serializers.ModelSerializer):
    phone_number = CharField(required=False)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number']

    @staticmethod
    def validate_first_name(value):
        if len(value) < 2:
            raise ValidationError("First name must be at least 2 characters long.")
        return value

    @staticmethod
    def validate_phone_number(value):
        if value and not value.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        return value


class MessageSerializer(serializers.ModelSerializer):
    sent_by = UserSerializer(read_only=True)
    message_preview = SerializerMethodField()

    class Meta:
        model = Message
        fields = ['message_id', 'message_body', 'sent_by', 'sent_at', 'message_preview']

    @staticmethod
    def get_message_preview(obj):
        return obj.message_body[:30]

    @staticmethod
    def validate_message_body(value):
        if not value.strip():
            raise ValidationError("Message body cannot be empty or only whitespace.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True, source='messages')

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
