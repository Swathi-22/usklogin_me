from django.db import models


class BroadcastNotification(models.Model):
    message = models.TextField()
    link = models.URLField(blank=True, null=True)
    broadcast_on = models.DateTimeField()
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ["-broadcast_on"]

    def __str__(self):

        return f"{self.message} - scheduled to {self.broadcast_on}"
