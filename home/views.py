from django.shortcuts import render
from home.models import Subjects, Exam, Question,Choice,File
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='login')
def detailExam(request,id):
    exam=Exam.objects.get(pk=id)
    list_questions_with_choices = []
    questions=Question.objects.filter(exam=exam.id)
    for question in questions:
        choices=Choice.objects.filter(question=question.id)
        question_with_choices = {
            'question': question,
            'choices': choices
        }
        list_questions_with_choices.append(question_with_choices)
    context={"list_Question": list_questions_with_choices,"exam":exam,}
    return render(request,'home/detailExam.html', context)

def result(request, id):
    exam=Exam.objects.get(pk=id)
    questions=Question.objects.filter(exam=exam.id)
    all=len(questions)
    true=0
    list_idchoice=request.POST.getlist('choice')
    for a in list_idchoice:
        choices=Choice.objects.get(pk=a)
        if choices.true is True:
            true=true+1 
    flase=all-true
    point=(all/10)*true   
    context={"trues": true,"exam":exam,"flases": flase,"point":point}
    return render(request,'home/result.html', context)


def detailResult(request,id):
    exam=Exam.objects.get(pk=id)
    list_questions_with_choices = []
    questions=Question.objects.filter(exam=exam.id)
    for question in questions:
        choices=Choice.objects.filter(question=question.id)
        question_with_choices = {
            'question': question,
            'choices': choices
        }
        list_questions_with_choices.append(question_with_choices)
    context={"list_Question": list_questions_with_choices,"exam":exam}
    return render(request,'home/detailResult.html', context)

def detailSubjects(request,id):
    subjects=Subjects.objects.get(pk=id)
    context={"List_subjects":subjects}
    return render(request,'home/detailSubjects.html', context)

def file(request):
    doc=File.objects.filter(status=True)
    paginator = Paginator(doc, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"doc":page_obj}
    return render(request,'home/file.html',context)

def tutorial(request):
    return render(request,'home/tutorials.html')