from rest_framework import mixins, viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .pagination import PaginationOption
from .serializers import SurveySerializer, QuestionSerializer, OptionSerializer, QuestionCreateSerializer, \
    QuestionEditSerializer
from ..models import Survey, Question, Option


class SurveyCreateListApiView(generics.ListCreateAPIView):
    queryset = Survey.objects.all().order_by("-start_at")
    serializer_class = SurveySerializer
    pagination_class = PaginationOption
    permission_classes = [IsAuthenticatedOrReadOnly]


class SurveyDetailEditDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    pagination_class = PaginationOption
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuestionListCreateApiView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        survey_pk = self.kwargs.get('survey_pk')
        survey = get_object_or_404(Survey, pk=survey_pk)
        serializer.save(survey=survey)

class QuestionDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionEditSerializer
    # serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OptionListCreateApiView(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        que_pk = self.kwargs.get('question_pk')
        question = get_object_or_404(Question, pk=que_pk)
        queryset = Option.objects.filter(question=question)
        serializer = OptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        que_pk = self.kwargs.get('question_pk')
        question = get_object_or_404(Question, pk=que_pk)
        if question.type == 'tex':
            Option.objects.filter(question=question).delete()
            raise ValidationError("No option required for this question!")
        serializer.save(question=question)


class OptionDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
