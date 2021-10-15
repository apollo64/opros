from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Survey, Question, Option, Participant
# from.forms import SurveyForm


class SurveyList(ListView):
    template_name = 'index.html'
    queryset = Survey.objects.order_by('-start_at')
    context_object_name = 'surveys'

#
# class SurveyAnswerold(DetailView):
#     template_name = 'survey.html'
#     queryset = Question.objects.order_by('question')


def SurveyAnswer(request, survey_pk):
    question = get_object_or_404( Question, id=survey_pk)
    # form = SurveyForm(request.POST or None, initial={'survey': survey})
    try:
        ryim = request.POST
        choosed_options= question.choice.get(pk=request.POST['option'])
    except (KeyError , Option.DoesNotExist):
        return render(request, "survey.html", {"question":question,
                                               "error_message":"Вы не выбрали.",} )
    else:
        choosed_options.vote +=1
        choosed_options.save()
        return HttpResponseRedirect(reverse('result', args=(question.survey.pk,)))
    # if form.is_valid():
    #     option_vote = form.cleaned_data
    #     ok=1
    # ok = 1
    # context = {
    #     'poll': survey
    # }
    # return render(request, 'survey.html', context)

def SurveyResult(request, question_id):
    question =get_object_or_404(Question, id = question_id)
    return render(request, "result.html", {"question":question})

#
# def SurveyAnswer2(request, poll_pk):
#     poll = Poll.objects.get(pk=poll_pk)
#
#     if request.method == 'POST':
#         print(request.POST['poll'])
#
#     context = {
#         'poll': poll
#     }
#     return render(request, 'poll/vote.html', context)
#
    # def vote(request):
    #     context = {}
    #     return render(request, 'survey.html', context)
