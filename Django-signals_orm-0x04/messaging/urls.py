from django.urls import path

from .views import delete_user,get_conversation_api

urlpatterns = [
    path('delete-account/', delete_user, name='delete_user'),
    path('get-conversation/', get_conversation_api, name='get_conversation_api'),
]
