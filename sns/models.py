from django.db import models
#각종 글작성시 효과 툴
from ckeditor_uploader.fields import RichTextUploadingField


class Question(models.Model):
    #생성된 게시글 숫자
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField()

    # 게시글 넘버링
    con_num = models.PositiveIntegerField(default=0)
    # 수정, 삭제 권한
    su_password = models.CharField(max_length=20)
    #조회수
    clik_num = models.PositiveIntegerField(default=0)
    def click(self):
        self.clik_num += 1
        self.save()
    #각종 글설정 툴
    content = RichTextUploadingField()


class Answer(models.Model):
    #참조시키기
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #
    name = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()
    an_password = models.CharField(max_length=20)


    #python manage.py migrate
    #python manage.py makemigrations