from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import (SurveyCreateListApiView, SurveyDetailEditDeleteApiView, \
    QuestionDetailApiView, QuestionListCreateApiView, OptionListCreateApiView, OptionDetailApiView)

urlpatterns = [
    path("surveys/", SurveyCreateListApiView.as_view(),
         name="survey-list"),
    path("survey/<int:pk>/", SurveyDetailEditDeleteApiView.as_view(),
         name="survey-detail"),
    path("survey/<int:survey_pk>/questions/", QuestionListCreateApiView.as_view(),
         name="survey-question"),
    path("question/<int:pk>/", QuestionDetailApiView.as_view(),
         name="question-detail"),
    path("question/<int:question_pk>/option/", OptionListCreateApiView.as_view(),
         name="que-options"),
    path("option/<int:pk>/", OptionDetailApiView.as_view(),
         name="options"),

]
