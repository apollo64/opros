from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import (SurveyCreateListApiView, SurveyDetailEditDeleteApiView, \
                    QuestionDetailApiView, QuestionListCreateApiView, OptionListCreateApiView, OptionDetailApiView,
                    # SurveyQuestionsCreateApiView
                    )

urlpatterns = [
    path("surveys/", SurveyCreateListApiView.as_view(),
         name="survey-list"),
    # path("survey/<int:pk>/", SurveyQuestionsCreateApiView.as_view(),
    #      name="survey-detail"),
    path("survey/<int:pk>/", SurveyDetailEditDeleteApiView.as_view(),
         name="survey-detail"),
    path("survey_questions/<int:survey_pk>/", QuestionListCreateApiView.as_view(),
         name="questions-list"),
    path("question/<int:pk>/", QuestionDetailApiView.as_view(),
         name="question-detail"),
    path("question_options/<int:question_pk>/", OptionListCreateApiView.as_view(),
         name="options-list"),
    path("option/<int:pk>/", OptionDetailApiView.as_view(),
         name="option-detail"),

]
