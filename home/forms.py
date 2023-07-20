from django import forms
from .models import Post, Student

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email']
