import time

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class Survey(models.Model):
    class Meta:
        ordering = ['-start_at']
        unique_together = ['start_at', 'finish_at']

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    start_at = models.DateField(auto_now_add=True)
    finish_at = models.DateField()
    active = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     from datetime import date
    #     today = date.today()
    #     print('finish at ', self.finish_at)
    #     print('today ', today)
    #
    #     if int(time.mktime(self.finish_at.timetuple())) >= today.timestamp():
    #     # if self.finish_at.timestamp() >= today.timestamp():
    #         print('ok')
    #         self.active = True
    #     super(Survey, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.start_at}"


class Question(models.Model):
    SINGLE_CHOICE = 'sin'
    MULTI_CHOICE = 'mul'
    TEXT_ANSWER = 'tex'
    TYPES = [(SINGLE_CHOICE, "Single_choice"),
             (MULTI_CHOICE, "Multi_choice"),
             (TEXT_ANSWER, "Text")]

    class Meta:
        ordering = ['-survey']

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="question")
    text = models.TextField(max_length=200, unique=True)
    type = models.CharField(max_length=3, choices=TYPES, default='tex')

    def __str__(self):
        return self.text


class Option(models.Model):
    class Meta:
        ordering = ['-question']

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option')
    text = models.CharField(max_length=100, blank=True, unique=True)
    vote = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        q = Question.objects.last()
        if q.type == 'tex' and q.option:
            raise ValidationError("Could not be any option as it is text question")
        super(Option, self).save(*args, **kwargs)

    def __str__(self):
        return self.text


class PartiSession(models.Model):
    '''users are defined by session_keys'''
    session_key = models.CharField(max_length=100, blank=True, null=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="participant", blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="user_question", blank=True,
                                 null=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="option_choosed", blank=True, null=True)
    answer_text = models.CharField(max_length=100, null=True, verbose_name='text_answer')

    # def clean(self):
    #     '''In case if there is no answer'''
    #     super().clean()
    #     if self.option is None and self.answer_text is None:
    #         raise ValidationError('Field  option and  answer_text  are empty!'
    #                               ' Must be filled at least one of')

    def __str__(self):
        return f"User with id: {self.pk}"

#
# class AnswerText(models.Model):
#     survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="user_answer")
#     question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
#     option = models.ForeignKey(Option, related_name="answers_to_option", on_delete=models.CASCADE)
#
# answer_tick = models.BooleanField(default=False)
