from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Survey, Question, Option, PartiSession


# from.forms import SurveyForm


class SurveyList(ListView):
    template_name = 'index.html'
    queryset = Survey.objects.order_by('-start_at')
    context_object_name = 'surveys'


class SurveyListResult(ListView):
    template_name = 'result_list.html'
    context_object_name = 'surveys_answered'

    def get_queryset(self):
        user_key = self.request.session_key
        user = PartiSession.objects.get_or_create(session_key=user_key)
        # user = PartiSession.objects.get(session_key = user_key)
        return Survey.objects.filter(session=user_key).order_by('-received_date')

"""Original """
def SurveyAnswer(request, survey_pk):
    question = get_object_or_404(Question, id=survey_pk)
    user_key = request.session.session_key

    try:
        choosed_options = question.choice.get(pk=request.POST['option'])

    except (KeyError, Option.DoesNotExist):
        return render(request, "survey.html", {"question": question,
                                               "error_message": "Вы не выбрали.", })
    else:
        survey = Survey.objects.get(question=question)
        user = PartiSession.objects.get_or_create(session_key=user_key)[0]
        user.question_id = question.pk
        user.survey_id = survey.pk
        user.save()
        choosed_options.vote += 1
        choosed_options.save()
        return HttpResponseRedirect(reverse('result', args=(question.survey.pk,)))


# def SurveyAnswer(request, survey_pk):
#     survey = Survey.objects.get(pk  = survey_pk)
#     # question = get_object_or_404(Question, id=survey_pk)
#     questions = Question.objects.filter(survey = survey)
#     user_key = request.session.session_key
#
#     try:
#         for question in questions:
#             choosed_option = question.choice.get(pk=request.POST['option'])
#
#
#
#         # choosed_options = question.choice.get(pk=request.POST['option'])
#
#
#     except (KeyError, Option.DoesNotExist):
#         return render(request, "survey.html", {"questions": questions,
#                                                "error_message": "Вы не ответили на все варианты.", })
#     else:
#         survey = Survey.objects.get(question=questions[0])
#         user = PartiSession.objects.get_or_create(session_key=user_key)[0]
#         user.question_id = question.pk
#         user.survey_id = survey.pk
#         user.save()
#         choosed_option.vote += 1
#         choosed_option.save()
#         return HttpResponseRedirect(reverse('result', args=(survey.pk,)))






def SurveyResult(request, question_id):
    questions = []
    '''todo: question_id change to survey and retreate info from Survey to results of votes '''
    session_key = request.session.session_key
    try:
        session = PartiSession.objects.get(session_key=session_key)
    except ValueError:
        print('There are no results for user with this session')
        return HttpResponseNotFound("hello")
    # questions = get_object_or_404(Question, user_question=session)
    question = Question.objects.filter(user_question=session)[0]
    survey_pk = question.survey.pk
    return render(request, "result.html", {"question": question,"survey_pk": survey_pk})
