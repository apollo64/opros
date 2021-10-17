from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Survey(models.Model):
    # participant = models.ForeignKey(Participant, on_delete=models.PROTECT, related_name="survey", blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField()

    def __str__(self):
        return f"{self.name}, {self.start_at}"

class Question(models.Model):
    SINGLE_CHOICE = 'sin'
    MULTI_CHOICE = 'mul'
    TEXT_CHOICE = 'tex'
    CHOICES = [(SINGLE_CHOICE, "Single_choice"),
               (MULTI_CHOICE, "Multi_choice"),
               (TEXT_CHOICE, "Text_choice")]
    # class Choice(models.TextChoices):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="question")
    text = models.TextField(max_length=200)
    type = models.CharField(max_length=3, choices=CHOICES, default=TEXT_CHOICE)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
    text = models.CharField(max_length=100, blank=True)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.text



class PartiSession(models.Model):
    # user= models.OneToOneField(User, default=None, on_delete=models.CASCADE, blank=True, related_name='session')
    session_key = models.CharField(max_length=100, blank=True, null=True)
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING, related_name="user", blank=True, null=True)
    question = models.ForeignKey(Question,on_delete=models.DO_NOTHING, related_name="user_question", blank=True, null=True)

    def __str__(self):
        return f"User with id: {self.pk}"

#
# class AnswerUser(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="user_answer")
#     question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
#     option = models.ForeignKey(Option, related_name="answers_to_option", on_delete=models.CASCADE)
#
    # answer_tick = models.BooleanField(default=False)
