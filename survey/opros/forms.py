from django.forms import ModelForm, forms, Form
from django import forms
from .models import Question, Survey, Option

#
# class SurveyForm(Form):
#     class Meta:
#         model=Survey
#         # exclude = ("types",)
#         fields = "__all__"
#         # options =
#         # poll_pk =
#         ok=1

# class SurveyForm(forms.Form):
# from django import forms
#
#
# class Aform(forms.From):
#     a  = forms.ModelMultipleChoiceField()

'original'


#
# class OptionForm(ModelForm):
#     options = forms.ModelMultipleChoiceField(queryset=Option.objects.all(),
#                                              widget=forms.CheckboxSelectMultiple)
#
#     ok = 1
#
#     class Meta:
#         model = Option
#         fields = ['text']


class OptionForm(ModelForm):
    """options related to one question"""

    def __init__(self, *args, **kwargs):
        super(OptionForm, self).__init__(*args, **kwargs)
        self.fields['options'] = forms.ModelMultipleChoiceField(queryset=Option.objects.filter(question=self.instance),
                                                                widget=forms.CheckboxSelectMultiple, required=True)
        self.fields['text'].disabled = True
    class Meta:
        model = Question
        fields = ['text']
