from django.contrib import admin
from django.urls import path, include

from .views import SurveyList, SurveyResult, SurveyListResult, SurveySpecQuesView
# SurveyAnswer,

urlpatterns = [
    path('', SurveyList.as_view(), name='survey_list'),
    path('answer/<int:survey_pk>/', SurveySpecQuesView, name='answer'),
    # path('answer/<int:survey_pk>/', SurveyAnswer, name='answer'),
    path('result/<int:question_id>/', SurveyResult, name='result'),
    path("userresults/<int:user_pk>/", SurveyListResult.as_view() , name= 'user_results' )
]