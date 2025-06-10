from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Message, MessageHistory, Notification


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )


@receiver(pre_save, sender=Message)
def log_message_history(sender, instance, **kwargs):
    if instance.id:
        try:
            old_instance = Message.objects.get(pk=instance.id)
            if old_instance.content != instance.content:
                MessageHistory.objects.create(
                    message=old_instance,
                    content=old_instance.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass  # message is new
