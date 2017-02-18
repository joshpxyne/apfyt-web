from .models import Answer, Question, Survey, SurveyResponse
from .serializers import AnswerSerializer, QuestionSerializer, SurveySerializer, SurveyResponseSerializer
from rest_framework import generics

# list views



class AnswerApiList(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class QuestionApiList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionApiListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SurveyApiList(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyResponseApiList(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveyResponseSerializer
