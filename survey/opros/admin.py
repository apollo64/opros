from django.contrib import admin

# Register your models here.
from .models import Option, Survey, Question, PartiSession

admin.site.register(PartiSession)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)

