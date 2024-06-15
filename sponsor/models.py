from django.conf import settings
from django.db import models
from home.models import *
from backend.models import *

class Letter(models.Model):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender', null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='receiver', null=True, blank=True)
    sponsor_name = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sponsor.email} - {self.student.name}"

class FavoriteStudent(models.Model):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_students')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='favorite_by')

    def __str__(self):
        return f"{self.sponsor.email} - {self.student.name}"

class SponsorDonateStudent(models.Model):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sponsor.email} -> {self.student.name}: ${self.amount}"