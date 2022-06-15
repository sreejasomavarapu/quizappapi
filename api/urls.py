
from django.urls import path,include
from  . views import home, questionsall, quiz, randomquestion
urlpatterns = [
    path('',home),
    path('quiz/',quiz.as_view()),
    path('r/question/<str:topic>',randomquestion.as_view()),
    path('q/<str:quiz>',questionsall.as_view())
    # I included spaces in the quiz name but idk how to include that in the url
]
