from django.conf.urls import url
from django.views.generic import TemplateView
from .api import (
	AnswerApiList, 
	QuestionApiList,
	QuestionApiListCreate,
	QuestionApiDetail,
	SurveyApiList,
	SurveyResponseApiList)

urlpatterns = [
	
	url(r'^$', TemplateView.as_view(template_name="surveys/survey.html")),

	url(r'^api/answer/$', AnswerApiList.as_view()),
	url(r'^api/questions/$', QuestionApiList.as_view()),
	url(r'^api/questions-list-create/$', QuestionApiListCreate.as_view()),
	url(r'^api/questions/(?P<pk>[0-9]+)/$', QuestionApiListCreate.as_view()),

	url(r'^api/surveys/$', SurveyApiList.as_view()),
	url(r'^api/survey-response/$', SurveyResponseApiList.as_view()),
]