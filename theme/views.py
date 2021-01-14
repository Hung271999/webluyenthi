from django.shortcuts import render
from django.template.response import TemplateResponse
from home.models import Subjects, Exam, Question,Choice
from django.core.paginator import Paginator
# Create your views here.

def homepage(request):
    list_exam=Exam.objects.order_by('date')[:20]
    paginator = Paginator(list_exam, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request, 'index.html',{'page_obj': page_obj})
