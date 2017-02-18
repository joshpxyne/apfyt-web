from django.contrib import admin

from .models import Answer, Question, Survey, SurveyResponse

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(SurveyResponse)

