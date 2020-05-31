from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.TextField()


class UserAskQuestion(models.Model):
    image = models.FileField(upload_to='media')
    question = models.ForeignKey(Question, related_name='+', on_delete=models.CASCADE)


class CatalogQuestions(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)


class SimilarQuestion(models.Model):
    catalog = models.ForeignKey(CatalogQuestions, related_name='similar_questions', on_delete=models.CASCADE, db_index=True)
    questions = models.ForeignKey(Question, related_name='similar', on_delete=models.CASCADE, db_index=True)


