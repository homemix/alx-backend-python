import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Conversation(models.Model):
    conversation_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    participants = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return self.conversation_id


class Message(models.Model):
    message_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    message_body = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_id
