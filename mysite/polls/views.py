# -*- coding: utf-8 -*-
# User:Administrator
# Last Update:2020-10-12 14:17
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    l_question = get_object_or_404(Question, pk=question_id)
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request,'templates/results.html', {'question':l_question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index1(request):
    latest_question_list = Question.objects.order_by('-l_date_publish')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged

def index(request):
    last_question_list = Question.objects.order_by('-l_date_publish')[:5]
    print(last_question_list)
    for i in last_question_list:
        print(i)
    from django.template import loader
    template = loader.get_template('templates/index.html')
    context = {
        'last_question_list': last_question_list
    }
    return HttpResponse(template.render(context, request))


from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail12(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
