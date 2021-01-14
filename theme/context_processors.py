from home.models import Subjects
def exam(request):
    list_subjects=Subjects.objects.all()
    context={"list_subjects":list_subjects}
    return(context)
