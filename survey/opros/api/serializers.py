
from rest_framework import serializers

from ..models import Question, Survey, Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"
        read_only_fields = ("vote","question",)

class QuestionSerializer(serializers.ModelSerializer):
    choice = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        # fields = "__all__"
        exclude = ("survey",)
        # read_only_fields =


class SurveySerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    # question =serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Survey
        fields = "__all__"
        read_only_fields = ("start_at",)

