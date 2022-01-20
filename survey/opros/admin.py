from django.contrib import admin

# Register your models here.
from .models import Option, Survey, Question, PartiSession



class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['id','type', 'survey']}),
    ]
    readonly_fields = ['survey', 'type', 'id',]
    inlines = [OptionInline]

class QuesInline(admin.TabularInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Type', {'fields': [ 'start_at',  'finish_at', 'description'] }),
    ]
    readonly_fields = ['id', 'start_at', 'active']
    inlines = [QuesInline]

admin.site.register(PartiSession)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)

