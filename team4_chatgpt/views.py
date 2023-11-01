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

    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            difficulty = form.cleaned_data['difficulty']
            num_questions = form.cleaned_data['num_questions']
            sentence = form.cleaned_data['sentence']

            openai.api_key = "YOUR_OPENAI_API_KEY"
            openai.api_base = "https://api.openai.iniad.org/api/v1"

            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Subject: {subject}\nDifficulty: {difficulty}\nNumber of Questions: {num_questions}\n{sentence}"}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            chat_results = response["choices"][0]["message"]["content"]
    else:
        form = ChatForm()

    template = loader.get_template('team4_chatgpt/index.html')
    context = {
        'form': form,
        'chat_results': chat_results
    }

    return HttpResponse(template.render(context, request))

