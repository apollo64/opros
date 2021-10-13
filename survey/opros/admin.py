from django.contrib import admin

# Register your models here.
from survey.opros.models import ChoiceQuestion, Survey, Question, Participant

admin.site.register(Participant)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(ChoiceQuestion)

