from django.conf.urls import url

from question.views import UploadQuestion, StudentViewVideo

urlpatterns = [
    url(r'^upload/$', UploadQuestion.as_view()),
    url(r'^view/$', StudentViewVideo.as_view()),
]
