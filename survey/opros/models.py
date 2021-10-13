from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Participant(User):
    pass


class Survey(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.PROTECT, related_name="survey")
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400,blank=True, null=True)
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()

    def __str__(self):
        return f"{self.name}, {self.started_at}"

class Question(models.Model):
    survey =models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="question")
    text = models.TextField(max_length= 200)


class ChoiceQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
    text = models.CharField(max_length=100)
    clicks = models.BooleanField(default=False)
    def __str__(self):
        return self.text


