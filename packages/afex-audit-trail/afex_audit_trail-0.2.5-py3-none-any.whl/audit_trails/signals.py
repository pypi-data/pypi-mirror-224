from django.dispatch import Signal

from audit_trails.models import Notification


class Notify:

    @staticmethod
    def create_notification_objects(actor_object_type, actor_object_id, recipients, level, **kwargs):
        recipient_ids = recipients.values_list('id', flat=True)
        notification_objects = [
            Notification(
                actor_object_type=actor_object_type,
                actor_object_id=actor_object_id,
                recipient_id=recipient_id,
                level=level,
                **kwargs
            )
            for recipient_id in recipient_ids
        ]
        return notification_objects

    def info(self, actor_object_type, actor_object_id, recipients, **kwargs):
        notification_objects = self.create_notification_objects(
            actor_object_type=actor_object_type,
            actor_object_id=actor_object_id,
            recipients=recipients,
            level='info',
            **kwargs
        )
        Notification.objects.bulk_create(notification_objects)
        # Notification.objects.bulk_create([
        #     Notification(actor_object_type=actor_object_type, actor_object_id=actor_object_id, recipient=recipient, level='info', **kwargs)
        #     for recipient in recipients
        # ])

    def success(self, actor_object_type, actor_object_id, recipients, **kwargs):
        notification_objects = self.create_notification_objects(
            actor_object_type=actor_object_type,
            actor_object_id=actor_object_id,
            recipients=recipients,
            level='success',
            **kwargs
        )
        Notification.objects.bulk_create(notification_objects)

    def warning(self, actor_object_type, actor_object_id, recipients, **kwargs):
        notification_objects = self.create_notification_objects(
            actor_object_type=actor_object_type,
            actor_object_id=actor_object_id,
            recipients=recipients,
            level='warning',
            **kwargs
        )
        Notification.objects.bulk_create(notification_objects)
        # Notification.objects.bulk_create([
        #     Notification(actor_object_type=actor_object_type, actor_object_id=actor_object_id, recipient=recipient, level='warning', **kwargs)
        #     for recipient in recipients
        # ])

    def error(self, actor_object_type, actor_object_id, recipients, **kwargs):
        notification_objects = self.create_notification_objects(
            actor_object_type=actor_object_type,
            actor_object_id=actor_object_id,
            recipients=recipients,
            level='error',
            **kwargs
        )
        Notification.objects.bulk_create(notification_objects)
        # Notification.objects.bulk_create([
        #     Notification(actor_object_type=actor_object_type, actor_object_id=actor_object_id, recipient=recipient, level='error', **kwargs)
        #     for recipient in recipients
        # ])


notify = Notify()
