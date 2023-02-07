from django import forms
from sns.models import Question
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'name', 'content', 'su_password']