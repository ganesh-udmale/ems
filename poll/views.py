from django.shortcuts import render, get_object_or_404
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
