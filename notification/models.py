from django.db import models


class BroadcastNotification(models.Model):
    message = models.TextField()
    broadcast_on = models.DateTimeField()
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ["-broadcast_on"]

    def __str__(self):
<<<<<<< HEAD
        return f"{self.message} - scheduled to {self.broadcast_on}"
=======
        return f'{self.message} - scheduled to {self.broadcast_on}'





@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
    # call group_send function directly to send notificatoions or you can create a dynamic task in celery beat
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(
            hour=instance.broadcast_on.hour, minute=instance.broadcast_on.minute, day_of_month=instance.broadcast_on.day, month_of_year=instance.broadcast_on.month
        )
        PeriodicTask.objects.create(
            crontab=schedule, name="broadcast-notification-" + str(instance.id), task="notifications_app.tasks.broadcast_notification", args=json.dumps((instance.id,))
        )

    # if not created:

>>>>>>> 5a9bf3a2834e2c8e93483661b7987ac1cab6730e
