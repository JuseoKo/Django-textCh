from django import forms
from sns.models import Question
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'name', 'content', 'su_password']
        labels = {
            'subject' : '제목',
            'name' : '작성자',
            'content' : '내용',
            'su_password' : '비밀번호',
        }
        help_texts = {
            'content': 'Some useful help text.'
        }
        widgets = {
            'content' : '하나찌'
        }