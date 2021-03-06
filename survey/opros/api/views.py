from rest_framework import mixins, viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .pagination import PaginationOption
from .serializers import SurveySerializer, QuestionSerializer, OptionSerializer
from ..models import Survey, Question, Option


class SurveyCreateListApiView(generics.ListCreateAPIView):
    queryset = Survey.objects.all().order_by("-start_at")
    serializer_class = SurveySerializer
    # pagination_class = PaginationOption
    permission_classes = [IsAuthenticatedOrReadOnly]


class SurveyDetailEditDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # pagination_class = PaginationOption
    permission_classes = [IsAuthenticatedOrReadOnly]

'''original'''
# class QuestionListCreateApiView(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         survey_pk = self.kwargs.get('survey_pk')
#         survey  = get_object_or_404(Survey, pk=survey_pk)
#         serializer.save(survey=survey)

class QuestionListCreateApiView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        survey_pk = self.kwargs.get('survey_pk')
        survey  = get_object_or_404(Survey, pk=survey_pk)
        serializer.save(survey=survey)


class QuestionDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

'''original '''
# class OptionListCreateApiView(generics.ListCreateAPIView):
#     queryset = Option.objects.all()
#     serializer_class = OptionSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         que_pk = self.kwargs.get('question_pk')
#         question  = get_object_or_404(Question, pk=que_pk)
#         if question.type == 'Tex':
#             option_queryset = Option.objects.filter(question=question)
#             if option_queryset.exists() is False:
#                 new_option = Option.objects.create(question=que_pk)
#                 serializer.save(question=question, option = new_option)
#             else:
#                 raise ValidationError("there are already options for the question created!")
#         elif question.type == 'Sin':
#             text = serializer.validated_date['text']
#             option_queryset = Option.objects.filter(question=question, text= text)
#             if option_queryset.exists():
#                 raise ValidationError("already exist!")
#         serializer.save(question=question)

class OptionListCreateApiView(generics.CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        que_pk = self.kwargs.get('question_pk')
        question  = get_object_or_404(Question, pk=que_pk)
        if question.type == 'Tex':
            option_queryset = Option.objects.filter(question=question)
            if option_queryset.exists() is False:
                new_option = Option.objects.create(question=que_pk)
                serializer.save(question=question, option = new_option)
            else:
                raise ValidationError("there are already options for the question created!")
        elif question.type == 'Sin':
            text = serializer.validated_date['text']
            option_queryset = Option.objects.filter(question=question, text= text)
            if option_queryset.exists():
                raise ValidationError("already exist!")
        serializer.save(question=question)



class OptionDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

