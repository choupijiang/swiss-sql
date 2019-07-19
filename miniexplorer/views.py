from django.shortcuts import render, get_object_or_404, redirect
from miniexplorer.models import Question
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from miniexplorer.forms import QuestionForm
# Create your views here.


def question_list(request):

    object_list = Question.objects.all()
    paginator = Paginator(object_list, 10)
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'explorer/question/list.html', {'questions': questions, 'page': page})



def question_detail(request, title):
    question = get_object_or_404(Question, title=title)
    return render(request, 'explorer/question/detail.html', {'question': question})


def question_create(request):
    if request.method == "POST":
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            # print(new_question)
            new_question.save()
            return redirect("./")
        else:
            print("x")
    else:
        form = QuestionForm()
    return render(request, "explorer/question/new.html", {'question_form': form})

