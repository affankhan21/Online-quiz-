from django.contrib import admin
from .models import Subject,Question ,Answer

class SubjectAdmin(admin.ModelAdmin):
    list_display=('id','sname')

class QuestionAdmin(admin.ModelAdmin):
    list_display=('id','question','marks','sname')



class AnswerAdmin(admin.ModelAdmin):
    list_display=('id','question','answer','is_correct',)

admin.site.register(Subject,SubjectAdmin)
admin.site.register(Question ,QuestionAdmin)     
admin.site.register(Answer ,AnswerAdmin)     

