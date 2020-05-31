import json

from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from question.models import UserAskQuestion
from question.tasks1 import pdf_task


class UploadQuestion(View):

    def post(self, request):
        print(request)
        u = UserAskQuestion(image=request.FILES['img'], question_id=request.POST['question_id'])
        u.save()

        return JsonResponse("OK")


class StudentViewVideo(View):

    @login_required
    def post(self, request):
        request.data = json.loads(request.body)
        question_id = request.data.get('question_id')
        user = request.user
        cache.set(f"reminder_question_{user.id}", question_id, 10*60)
        pdf_task.apply_async((question_id, user.id), countdown=5*60)
        return JsonResponse('OK')
