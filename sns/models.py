from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()


    #python manage.py migrate
    #python manage.py makemigrations