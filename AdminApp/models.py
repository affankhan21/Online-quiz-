from django.db import models

class Subject(models.Model):
    sname = models.CharField(max_length=30)

    class Meta:
        db_table = "Subject"

    def __str__(self):
        return self.sname    

class Question(models.Model):
    question = models.CharField(max_length=300)
    marks = models.IntegerField(default=5)
    sname = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = "Question"

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "Answer"
