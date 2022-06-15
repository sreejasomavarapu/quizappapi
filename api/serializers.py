from dataclasses import fields
from rest_framework import serializers
from .models import *


# URL CAN NEVER BE UPPER CASE, AS WE ARE PASSING CATEGORY IN THE URL AND EXTRACTING IT FROM URL
# CATEGORIES SHOULD ALWAYS BE LOWERCASE 

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['title']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields=['id','body','is_right']


class QuestionSerializer(serializers.ModelSerializer):
    #answer = serializers.StringRelatedField(many=True)
    answer=AnswerSerializer(many=True)
    quiz = QuizSerializer()
    # gave related name as answer for fk of question in answer table
    class Meta:
        model = Question
        fields=['quiz','title','answer']


  


