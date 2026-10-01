from django.shortcuts import render
from .models import Question


def select(request):
    return render(request, 'select.html')


def test(request):
    number = int(request.GET.get('number', 1))

    questions = Question.objects.order_by('?')[:number]

    return render(request, 'test.html', {
        'questions': questions
    })


def result(request):

    score = 0
    total = 0

    if request.method == 'POST':

        for key, value in request.POST.items():

            if key.startswith('question_'):

                question_id = key.replace('question_', '')

                try:
                    question = Question.objects.get(id=question_id)

                    total += 1

                    if value == question.answer:
                        score += 1

                except Question.DoesNotExist:
                    pass

    return render(request, 'result.html', {
        'score': score,
        'total': total
    })