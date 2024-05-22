from django.db import models
from AdminApp.models import Subject,Question
from datetime import datetime

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=150,primary_key=True)
    password  = models.CharField(max_length=128)
    email = models.EmailField(max_length = 100)
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)

    class Meta:
        db_table = "UserInfo"

    def __str__(self):
        return self.username
from django.db import models
from AdminApp.models import Subject

class Test(models.Model):
    user = models.ForeignKey('UserApp.UserInfo', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)  # Automatically set the date/time when the test is created
    duration_minutes = models.IntegerField(default=0, verbose_name='Duration (minutes)')  # Duration of the test in minutes
    # Add other fields as needed

    class Meta:
        db_table = "Test"

    def __str__(self):
        return f"{self.user.username}'s test on {self.subject.sname}"
