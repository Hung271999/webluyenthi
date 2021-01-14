from django.contrib import admin
from tinymce.widgets import TinyMCE
# Register your models here.
from django.db import models
from .models import Subjects, Exam, Question,Choice,File
admin.site.register(Subjects)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(File)