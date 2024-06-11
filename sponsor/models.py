from django.db import models
from home.models import *
from backend.models import *

class Letter(models.Model):
    sender = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sent_letters')
    receiver = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='received_letters')
    slug = models.SlugField(unique=True, blank=True)
    letter = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.sender.firstname}-{self.receiver.name}-{timezone.now()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Letter from {self.sender.firstname} to {self.receiver.name}"