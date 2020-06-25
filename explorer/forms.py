from django.forms import ModelForm
from .models import questions, answers, Post

class QuestionForm(ModelForm):
    class Meta:
        model = questions
        fields = ['First_Name','Last_Name', 'Email','Subject', 'description']

class AnswerForm(ModelForm):
    class Meta:
        model = answers
        fields = ['First_Name','Last_Name', 'Email','Subject','img','description']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['First_Name','Last_Name', 'Email','title','img', 'Subject', 'description']