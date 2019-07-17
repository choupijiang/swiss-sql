from django.shortcuts import render, get_object_or_404
from miniexplorer.models import Question
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def question_list(request):
    # questions = Question.objects.all()
    # return render(request, 'explorer/question/list.html', {'questions': questions})\
    object_list = Question.objects.all()
    paginator = Paginator(object_list, 10)
    page = request.GET.get("post")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'explorer/question/list.html', {'questions': questions})



def question_detail(request, title):
    question = get_object_or_404(Question, title=title)
    return render(request, 'explorer/question/detail.html', {'question': question})



