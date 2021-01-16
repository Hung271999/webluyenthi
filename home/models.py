from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Subjects(models.Model):
    title=models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Exam(models.Model):
    title=RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    level=models.IntegerField()
    number=models.IntegerField()
    subjects=models.ManyToManyField(Subjects)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
class Question(models.Model):
     body=RichTextField(null=True, blank=True)
     exam= models.ManyToManyField(Exam)

     def __str__(self):
        return self.body


class Choice(models.Model):
   body=RichTextField(null=True, blank=True)
   question= models.ForeignKey(Question, on_delete=models.CASCADE)
   true=models.BooleanField(default=False)
   def __str__(self):
        return self.body

class File(models.Model):
    title =RichTextField(null=True, blank=True)
    link_url = models.URLField(max_length=255, unique=True)
    image = models.ImageField(null=True, blank=True)
    status=models.BooleanField(default=True)
    subjects= models.ForeignKey(Subjects, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.title




