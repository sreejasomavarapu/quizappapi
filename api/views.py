from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from . models import Quiz, Question
from api.serializers import QuizSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def home(request):
    return HttpResponse("Hello")

class quiz(generics.ListAPIView):
    serializer_class=QuizSerializer
    queryset = Quiz.objects.all()

# URL CAN NEVER BE UPPER CASE, AS WE ARE PASSING CATEGORY IN THE URL AND EXTRACTING IT FROM URL
# CATEGORIES SHOULD ALWAYS BE LOWERCASE 


class randomquestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__category__name=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionSerializer(question,many=True)
        # dont forget many=True
        # idk why i got error when i didnt use it
        # even though im serializing only one object
        # We can also serialize querysets instead of model instances.
        #  To do so we simply add a many=True flag to the serializer arguments.
        # we use many=True for querysets
        return Response(serializer.data)

class questionsall(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['quiz'])
        serializer = QuestionSerializer(question,many=True)
        return Response(serializer.data)




