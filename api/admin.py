from django.contrib import admin
from . models import *
# Register your models here.

class AnswerInline(admin.TabularInline):
    model=Answer
    #extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
    (None,{'fields':['title','quiz','technique','difficulty']}),
    ('Date Information',{'fields':[],'classes':['collapse']}) 
    # this is editable as we did auto_now_add so we get an error if we put it here. We need to import 
    # timezone to get editable one
    ]
    inlines=[AnswerInline]
admin.site.register(Question,QuestionAdmin)
admin.site.register(Category)
admin.site.register(Quiz)
