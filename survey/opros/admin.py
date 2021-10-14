from django.contrib import admin

# Register your models here.
from .models import Option, Survey, Question, Participant

admin.site.register(Participant)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)

