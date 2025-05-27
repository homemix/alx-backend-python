from django.urls import include, path
from rest_framework import routers

from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
