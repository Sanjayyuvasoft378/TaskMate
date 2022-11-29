from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CommonModel(models.Model):
    createdOn = models.DateTimeField()
    createdBy = models.CharField(max_length=10)
    updatedOn = models.DateTimeField()
    updatedBy = models.CharField(max_length=20)



class TestTaskModel(CommonModel):
    image = models.ImageField(upload_to='testing')
    name = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    testimonial_description = models.TextField(max_length=200)

    class Meta:
        db_table = "Task"
    def __str__(self):
        return self.name



class TodoListModel(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task +"-"+str(self.done)