import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} ({self.email})"


class Conversation(models.Model):
    conversation_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.conversation_id)


class Message(models.Model):
    message_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    message_body = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} in Conversation {self.conversation_id}"
