from django.shortcuts import render
from django.utils import timezone

from .models import Question
from .models import QuestionField


def index(request):
    latest_questions = Question.objects.order_by('-date_published')[:6]
    if request.method == 'POST':
        field = QuestionField(request.POST)
        if field.is_valid():
            question = Question(question_text=request.POST['question_text'],
                                date_published=timezone.now())
            question.save()

    else:
        field = QuestionField()

    return render(request, 'q/index.html',
                  {'field': field, 'latest_questions': latest_questions})
