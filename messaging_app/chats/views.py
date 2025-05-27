from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(ViewSet):
    queryset = Conversation.objects.all()

    def list(self, request):
        # conversations = Conversation.objects.all()
        serializer = ConversationSerializer(self.queryset, many=True)
        return Response(serializer.data)


class MessageViewSet(ViewSet):
    queryset = Message.objects.all()

    def list(self, request):
        # messages = Message.objects.all()
        serializer = MessageSerializer(self.queryset, many=True)
        return Response(serializer.data)
