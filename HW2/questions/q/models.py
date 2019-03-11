from django.db import models
from django.forms import ModelForm


class Question(models.Model):
    question_text = models.CharField(max_length=228)
    date_published = models.DateTimeField('published')

    def __str__(self):
        return self.question_text


class QuestionField(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
