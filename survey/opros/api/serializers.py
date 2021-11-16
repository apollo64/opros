
from rest_framework import serializers

from ..models import Question, Survey, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        exclude = ('vote',)
        read_only_fields = ("question",)

class QuestionSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'text', 'type', 'survey', 'option')
        # fields = "__all__"
        # exclude = ("survey",)
        read_only_fields = ("survey",)

class QuestionOnlySerializer(serializers.ModelSerializer):
    # choice = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        # fields = "__all__"
        exclude = ("survey",)

class SurveySerializer(serializers.ModelSerializer):
    # question = QuestionOnlySerializer(many=True, read_only=True)
    question = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='question-detail'
    )
    # question =serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Survey
        # fields = "__all__"
        fields = ('name','description',
                  'start_at','finish_at',
                  'active', 'question')

        read_only_fields = ("start_at","active")

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields= ("__all__",)


class QuestionEditSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('text','type', 'survey','option')
        extra_kwargs = {
            'type': {'read_only': True},
            'survey': {'read_only': True},
        }
