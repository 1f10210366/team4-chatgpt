from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .forms import ChatForm

def index(request):
  

  form = ChatForm()
  template = loader.get_template('team4_chatgpt/templates/team4_chargpt/index.html')
  context = {
    'form':form
  }
  return HttpResponse(template.render(context,request))


