from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


# URL CAN NEVER BE UPPER CASE, AS WE ARE PASSING CATEGORY IN THE URL AND EXTRACTING IT FROM URL
# CATEGORIES SHOULD ALWAYS BE LOWERCASE 

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,default=1)
    title= models.CharField(max_length=100, default=_("New Title"),verbose_name=_("Quiz Title"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    class Meta:
        abstract = True

class Question(Updated):
    class Meta:
        verbose_name =_("Question")
        verbose_name_plural =_("Questions")
        ordering = ['id']
        
    SCALE =(
        (0,_('School')),
        (1,_('Basic')),
        (2,_('Intermediate')),
        (3,_('Advanced')),
        (4,_('Expert')),
    )
    TYPE =(
        ('MCQ','MCQ'),
        ('Descriptive','Descriptive'),
        ('True or False','True or False'),
    )

    difficulty = models.IntegerField(choices=SCALE, verbose_name=_("Difficulty"))
    quiz = models.ForeignKey(Quiz,on_delete=models.DO_NOTHING, related_name='question')
    technique = models.CharField(max_length=100,choices=TYPE, verbose_name=_("Technique"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    title= models.CharField(max_length=100, default=_("New Question"),verbose_name=_("Question"))
    
    def __str__(self):
        return self.title

class Answer(Updated):

    class Meta:
        verbose_name =_("Answer")
        verbose_name_plural =_("Answers")
        ordering = ['id']

    question = models.ForeignKey(Question,on_delete=models.DO_NOTHING,related_name='answer')
    is_right = models.BooleanField()
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.body
