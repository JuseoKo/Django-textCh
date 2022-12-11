from django import forms
from sns.models import Question

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