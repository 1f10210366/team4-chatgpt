from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from .forms import ChatForm

from django.views.generic import CreateView
from django.urls import reverse_lazy

import openai

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


from . import forms

#signup
from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import SignUpForm


class Newstudent(TemplateView):
    template_name = "team4_chatgpt/newstudent.html"

class TopView(TemplateView):
    template_name = "team4_chatgpt/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "team4_chatgpt/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "team4_chatgpt/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "team4_chatgpt/logout.html"

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "team4_chatgpt/home.html"

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "team4_chatgpt/signup.html"
    success_url = reverse_lazy("team4_chatgpt:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
    

# views.py

def index(request):
    chat_results = ""
    response = None
    form = ChatForm(request.POST)  # フォームの初期化を修正

    if request.method == "POST" and form.is_valid():  # フォームが有効であるかを確認
        subject = form.cleaned_data['subject']
        difficulty = form.cleaned_data['difficulty']
        num_questions = form.cleaned_data['num_questions']
    
        openai.api_key = "wprzlNppD6DwlmSTfw35yGnUyaQ8XwfqnFKAnxB6WAjOaRp641FrM91T_NY1E05F6DyW6iIMsmJVSjuyKU8NZsg"
        openai.api_base = "https://api.openai.iniad.org/api/v1"

        messages = [
            {"role": "system", "content": "問題作成に特化したAI"},
            {"role": "user", "content": f"{subject}で難易度は{difficulty}な問題を{num_questions}作成してください。問題は一問づつ改行してください"}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

    if response:
        chat_results = response["choices"][0]["message"]["content"]

    template = loader.get_template('team4_chatgpt/index.html')
    context = {
        'form': form,
        'chat_results': chat_results
    }

    return HttpResponse(template.render(context, request))


def text(request):
    chat_results = ""  # 'chat_results' の初期化


    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']


            openai.api_key = "wprzlNppD6DwlmSTfw35yGnUyaQ8XwfqnFKAnxB6WAjOaRp641FrM91T_NY1E05F6DyW6iIMsmJVSjuyKU8NZsg"
            openai.api_base = "https://api.openai.iniad.org/api/v1"


            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"{sentence}"}
                ]
            )


            chat_results = response["choices"][0]["message"]["content"]


    else:
        form = ChatForm()


    template = loader.get_template('team4_chatgpt/newtext.html')
    context = {
        'form': form,
        'chat_results': chat_results  # 変数名を 'chat_results' に修正
    }


    return HttpResponse(template.render(context, request))


    
