from django import forms
from .models import Diary
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['write'] # id 속성은 PK 이므로 사용하지 않음

        labels = { # fields에 명시된 속성만 사용
        'write': '일기'
        }
