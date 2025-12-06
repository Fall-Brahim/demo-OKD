from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    visited_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-visited_at']

    def __str__(self):
        return f"{self.name} - {self.visited_at.strftime('%Y-%m-%d %H:%M')}"

