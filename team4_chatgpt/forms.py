from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChatForm(forms.Form):

  sentence = forms.CharField(label='チャット', widget=forms.Textarea(), required=True)


class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# forms.py

from django import forms

class ChatForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    difficulty = forms.ChoiceField(choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")], required=True)
    num_questions = forms.IntegerField(min_value=1, max_value=10, required=True)
    sentence = forms.CharField(widget=forms.Textarea, required=True)

