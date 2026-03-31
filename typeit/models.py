from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Passage(models.Model):
    text = models.TextField()
    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.difficulty} Passage"

class TypingRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField()
    total_chars = models.IntegerField()
    correct_chars = models.IntegerField()
    errors = models.IntegerField()

    wpm = models.FloatField()
    accuracy = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.wpm} WPM"
