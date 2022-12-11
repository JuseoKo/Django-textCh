from django.db import models


class Question(models.Model):
    #생성된 게시글 숫자
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()


    # 게시글 넘버링
    con_num = models.PositiveIntegerField(default=0)
    # 수정, 삭제 권한
    su_password = models.CharField(max_length=20)
    #생성된 게시글 수
    # def num(self):
    #     self.con_num += 1
    #     self.save()
    #조회수
    clik_num = models.PositiveIntegerField(default=0)
    def click(self):
        self.clik_num += 1
        self.save()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()


    #python manage.py migrate
    #python manage.py makemigrations