from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from poll.models import *


# Create your views here.


def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)

def details(request, id):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request, 'polls/details.html', context)

def vote_poll(request, id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context["question"] = question

    if request.method == "POST":
        user_id = 1
        print(request.POST)
        data = request.POST
        ret = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponseRedirect(reverse('poll_details', args=[question.id]))
        else:
            context["error"] = "Your vote is not done successfully"
            return render(request, 'polls/poll.html', context)
    else:
        return render(request, 'polls/poll.html', context)
