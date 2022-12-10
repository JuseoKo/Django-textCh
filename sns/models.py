from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()
    #조회수
    clik_num = models.PositiveIntegerField(default=0)
    def click(self):
        self.clik_num += 1
        self.save()
        #


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()


    #python manage.py migrate
    #python manage.py makemigrations