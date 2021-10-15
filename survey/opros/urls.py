from django.contrib import admin
from django.urls import path, include

from .views import SurveyList, SurveyAnswer, SurveyResult

urlpatterns = [
    path('', SurveyList.as_view(), name='survey_list'),
    path('answer/<int:survey_pk>/', SurveyAnswer, name='answer'),
    path('result/<int:question_id>/', SurveyResult, name='result'),
]